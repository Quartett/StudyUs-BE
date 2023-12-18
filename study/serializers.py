from rest_framework import serializers
from .models import Comment, StudyGroup, StudyMember

class CommentSerializer(serializers.ModelSerializer):
    # 댓글에 대한 유저의 이름을 보여주기 위해 추가
    author_nickname = serializers.SerializerMethodField()
    # 댓글에 대한 답글을 보여주기 위해 추가
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'parent', 'study_group', 'author', 'author_nickname', 'text', 'created_at', 'reply']
        read_only_fields = ['author']


    def get_author_nickname(self, obj):
        '''
        get_author_username 함수가 serializers.SerializerMethodField()의 반환값이 되어author_username 에 삽입
        Django REST Framework는 해당 필드에 대한 값을 얻기 위해 get_<field_name> 형식의 메서드를 호출
        '''
        return obj.author.nickname  # 댓글 작성자의 사용자 이름 반환
    
    def get_reply(self, obj):
        '''
        get_reply 함수가 serializers.SerializerMethodField()의 반환값이 되어 reply 에 삽입
        '''
        # 댓글에 대한 답글을 반환
        if obj.reply:
            return CommentSerializer(obj.reply, many=True).data
        return None

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class StudyGroupSerializer(serializers.ModelSerializer):
    chat_room_id = serializers.SerializerMethodField()    
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = StudyGroup
        fields = ['id', 'author', 'thumbnail', 'title', 'category', 'content', 'created_at', 'updated_at', 'study_start_at', 'study_end_at', 'max_members', 'comments', 'chat_room_id']
        read_only_fields = ['author']


    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    def get_chat_room_id(self, obj):
        return obj.chat_room.id

class MemberSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()

    class Meta:
        model = StudyMember
        fields = ['id', 'study_group', 'user', 'user_nickname', 'role']
        read_only_fields = ['user']


    def get_user_nickname(self, obj):
        return obj.user.nickname


class UpdateMemberSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()

    class Meta:
        model = StudyMember
        fields = ['id', 'study_group', 'user', 'user_nickname', 'role']
        read_only_fields = ['study_group','role']

    
    def get_user_nickname(self, obj):
        return obj.user.nickname