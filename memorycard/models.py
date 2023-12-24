from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user', 'title')

        
class MemoryCard(models.Model):

    class Difficultys(models.IntegerChoices):
        EASY = 1
        NORMAL = 2
        HARD = 3


    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    memory_question = models.TextField()
    memory_answer = models.TextField()
    bookmark = models.BooleanField(default=False)
    difficulty = models.IntegerField(choices=Difficultys.choices, default=Difficultys.EASY)

    class Meta:
        ordering = ['-id']