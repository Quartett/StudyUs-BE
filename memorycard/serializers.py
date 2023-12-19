from rest_framework import serializers
from .models import Subject, MemoryCard
from django.db import IntegrityError

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'user', 'title')
        read_only_fields = ('user',)


class MemoryCardSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = MemoryCard
        fields = ('id', 'subject', 'memory_question', 'memory_answer', 'bookmark', 'difficulty')
        read_only_fields = ('subject',)
