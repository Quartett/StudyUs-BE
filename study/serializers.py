from rest_framework import serializers
from .models import Comment, StudyGroup, StudyMember
from accounts.models import StudyUsUser

class CommentSerializer(serializers.ModelSerializer):
    # 댓글에 대한 유저의 이름을 보여주기 위해 추가
    author_nickname = serializers.SerializerMethodField()
    # 댓글에 대한 답글을 보여주기 위해 추가
    reply = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'parent', 'study_group', 'author', 'author_nickname', 'text', 'created_at', 'reply', 'profile_image']
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
    
    def get_profile_image(self, obj):
        # author의 id를 통해서 StudyUsUser의 profile_image를 가져옴
        author = StudyUsUser.objects.get(id=obj.author.id)
        return author.profile_image.url if author.profile_image else None


class MemberSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = StudyMember
        fields = ['id', 'study_group', 'user', 'user_nickname', 'role', 'profile_image']
        read_only_fields = ['user']


    def get_user_nickname(self, obj):
        return obj.user.nickname
    
    def get_profile_image(self, obj):
        # 멤버의 프로필 이미지를 보여주기 위해 추가
        return obj.user.profile_image.url if obj.user.profile_image else None


class UpdateMemberSerializer(serializers.ModelSerializer):
    user_nickname = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = StudyMember
        fields = ['id', 'study_group', 'user', 'user_nickname', 'role', 'profile_image']
        read_only_fields = ['study_group','role']

    
    def get_user_nickname(self, obj):
        return obj.user.nickname
    
    def get_profile_image(self, obj):
        # 멤버의 프로필 이미지를 보여주기 위해 추가
        return obj.user.profile_image.url if obj.user.profile_image else None


class StudyGroupSerializer(serializers.ModelSerializer):
    chat_room_id = serializers.SerializerMethodField()    
    comments = CommentSerializer(many=True, read_only=True)
    leader = serializers.SerializerMethodField()

    class Meta:
        model = StudyGroup
        fields = ['id', 'thumbnail', 'title', 'level', 'week_days', 'category', 'content', 'created_at', 'updated_at', 'study_start_at', 'study_end_at', 'max_members', 'comments', 'chat_room_id', 'leader']


    def get_chat_room_id(self, obj):
        return obj.chat_room.id
    
    def get_leader(self, obj):
        leader = StudyMember.objects.filter(study_group=obj, role=1).first()
        if leader:
            leader_info = StudyUsUser.objects.get(id=leader.user.id)
            return {
                'nickname': leader_info.nickname,
                'profile_image': leader_info.profile_image.url if leader_info.profile_image else None
            }
        return None