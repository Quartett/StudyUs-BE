import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        chat_history = await self.get_chat_history()
        for chat in chat_history:
            await self.send(text_data=json.dumps({"message": chat.content}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # user = self.scope["user"]
        room_id = text_data_json["room_id"]
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
        await self.save_message(room_id, message)

    @database_sync_to_async
    def save_message(self, room_id, message):
        Chat.objects.create(room=ChatRoom.objects.get(id=room_id), content=message)

    @database_sync_to_async
    def get_chat_history(self):
        chat_history = Chat.objects.filter(room__id=self.room_name)
        return list(chat_history)