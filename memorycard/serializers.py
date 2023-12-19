from rest_framework import serializers
from .models import MemoryCard

class MemoryCardSerailizer(serializers.ModelSerializer):
    class Meta:
        model = MemoryCard
        fields = ('id', 'user', 'memory_question', 'memory_answer', 'bookmark')
        read_only_fields = ('user',)