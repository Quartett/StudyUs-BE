from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class StudyGroup(models.Model):
    group_name = models.CharField(max_length=30)
    max_member = models.IntegerField()
    current_member = models.IntegerField()
    role = models.CharField(max_length=30)

class Comment(models.Model):
    studygroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.text}'
    