from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ["id", "user", "user_nickname", "content", "created_at"]

    def get_user_nickname(self, obj):
        return obj.user.nickname