from django.db import models
from django.conf import settings
from chat.models import ChatRoom


class Category(models.Model):
    category_name = models.CharField()


class StudyGroup(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='study_id') 
    image = models.ImageField(upload_to = 'study_images/')
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    study_start_at = models.DateTimeField(auto_now_add=True)
    studu_end_at = models.DateTimeField(auto_now_add=True)
    max_members = models.IntegerField()
    chatroom_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='study')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='study_id')


class StudyMember():
    member_id = models.IntegerField(settings.AUTH_USER_MODEL,  primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='studygroup') 
    study_id = models.TextField()
    # role = models.BooleanField()


class Comment(models.Model):
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.text}'
