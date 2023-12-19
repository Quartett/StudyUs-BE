from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MemoryCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memory_question = models.TextField()
    memory_answer = models.TextField()
    bookmark = models.BooleanField(default=False)