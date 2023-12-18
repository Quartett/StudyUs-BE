from django.contrib import admin
from .models import StudyGroup, StudyMember, Comment, Category

admin.site.register(StudyGroup)
admin.site.register(StudyMember)
admin.site.register(Comment)
admin.site.register(Category)
