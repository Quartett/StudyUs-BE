import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        '''
        1) 요청이 들어온 스코프에서 URL을 추출해 room_name을 지정함
        2) chat_방이름으로 그룹 네임을 설정함
        3) 비동기로 채널 계층에 그룹을 생성함
        4) 해당 그룹 ID에 이전 대화 기록이 있다면 반환
        '''
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        chat_history = await self.get_chat_history()
        for chat in chat_history:
            await self.send(text_data=json.dumps({
                "message": chat.content, 
                "nickname": await database_sync_to_async(lambda: chat.user.nickname)(),
                "profile_image": await database_sync_to_async(lambda: chat.user.profile_image.url)(),    
            }))
            
    async def disconnect(self, close_code):
        '''
        소켓 연결이 끊어졌을 때
        채널 계층에서 그룹을 버림
        '''
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        '''
        데이터를 받았을 때,
        비동기로 그룹 모두에게 전송
        '''
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        room_id = text_data_json["room_id"]
        user_id = text_data_json['user_id']
        nickname = await database_sync_to_async(lambda: User.objects.get(id=user_id).nickname)()
        profile_image = await database_sync_to_async(lambda: User.objects.get(id=user_id).profile_image.url)()
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "room_id": room_id, "nickname": nickname, "profile_image": profile_image, "user_id": user_id}
        )
        await self.save_message(room_id, message, user_id)

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message,
            "nickname": event["nickname"],
            "profile_image": event["profile_image"],
        }))

    @database_sync_to_async
    def save_message(self, room_id, message, user_id):
        '''
        전송한 채팅을 DB에 비동기로 저장
        '''
        Chat.objects.create(chat_room=ChatRoom.objects.get(study_group__id=room_id), content=message, user=User.objects.get(id=user_id))

    @database_sync_to_async
    def get_chat_history(self):
        '''
        비동기로 이전 대화기록이 있는지 확인해서 list를 반환
        '''
        chat_history = Chat.objects.filter(chat_room__id=self.room_name)
        return list(chat_history)
