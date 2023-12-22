from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    category_name = models.CharField()


class StudyGroup(models.Model):
  
    class Difficultys(models.IntegerChoices):
        EASY = 1
        NORMAL = 2
        HARD = 3

    class Weeks(models.IntegerChoices):
        월 = 1
        화 = 2
        수 = 3
        목 = 4
        금 = 5
        토 = 6
        일 = 7
        
    thumbnail = models.ImageField(upload_to = 'study_images/', blank=True)
    title = models.TextField()
    level = models.IntegerField(choices=Difficultys.choices, default=Difficultys.EASY)
    week_days = models.TextField(choices=Weeks.choices, default=Weeks.월, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    study_start_at = models.DateField(blank=True)
    study_end_at = models.DateField(blank=True)
    max_members = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True, null=True)


class StudyMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='study_group')
    role = models.IntegerField(default=0)

    class Meta:
        unique_together = ('study_group', 'user')


    def __str__(self):
        return f'{self.study_group.title}그룹 - {self.role} - {self.user}'


class Comment(models.Model):
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'작성자:{self.author.nickname} - {self.text}'
