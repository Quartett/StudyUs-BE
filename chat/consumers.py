import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom

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
            await self.send(text_data=json.dumps({"message": chat.content}))

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
        nickname = self.scope['user'].nickname
        # profile_image = self.scope['user'].profile_image.url | 'https://source.unsplash.com/random/300×300' // 프로필 기본설정 완료 되면 주석 풀 것
        room_id = text_data_json["room_id"]
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "nickname": nickname} # 추후 profile_image 추가
        )
        await self.save_message(room_id, message)

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def save_message(self, room_id, message):
        '''
        전송한 채팅을 DB에 비동기로 저장
        '''
        Chat.objects.create(chat_room=ChatRoom.objects.get(study_group__id=room_id), content=message, user=self.scope["user"])

    @database_sync_to_async
    def get_chat_history(self):
        '''
        비동기로 이전 대화기록이 있는지 확인해서 list를 반환
        '''
        chat_history = Chat.objects.filter(chat_room__id=self.room_name)
        return list(chat_history)