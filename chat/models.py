from django.db import models
from study.models import StudyGroup
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatRoom(models.Model):
    study_group = models.OneToOneField(StudyGroup, on_delete=models.CASCADE, related_name='chat_room')


class Chat(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='chats')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
