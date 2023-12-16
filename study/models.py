from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    category_name = models.CharField()


class StudyGroup(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_id') 
    thumnail = models.ImageField(upload_to = 'study_images/', blank=True)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    study_start_at = models.DateTimeField(auto_now_add=True)
    study_end_at = models.DateTimeField(auto_now_add=True)
    max_members = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True)


class StudyMember():
    member_id = models.IntegerField(User,  primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studygroup') 
    study_id = models.TextField()
    # role = models.BooleanField()


class Comment(models.Model):
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.text}'
