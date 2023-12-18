from django.shortcuts import render
from rest_framework import generics, permissions
from .models import StudyGroup, Comment, StudyMember
from chat.models import ChatRoom
from .serializers import CommentSerializer, StudyGroupSerializer, MemberSerializer, UpdateMemberSerializer
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import views, response, status
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model
from .permissions import MemberOnly

User = get_user_model()

class StudygroupListAPIView(generics.ListAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class StudygroupCreateView(generics.CreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        ChatRoom.objects.create(study_group=serializer.instance)


class StudygroupRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class StudygroupUpdateAPIView(generics.UpdateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class StudygroupDestroyAPIView(generics.DestroyAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    @extend_schema(
        summary='댓글 리스트',
    )

    def get_queryset(self):
        return self.queryset.filter(study_group_id=self.kwargs['study_group_id'])


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class JoinMemberView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        summary='그룹 참가',
        request=MemberSerializer
    )

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            study_group = serializer.validated_data['study_group']
            role = serializer.validated_data['role']
            member, created = StudyMember.objects.get_or_create(study_group=study_group, user=request.user, role=role)

            if not created:
                # 이미 참여중인 경우, 409 Conflict 반환
                return response.Response(status=status.HTTP_409_CONFLICT)
            return response.Response(status=status.HTTP_201_CREATED)


class MemberListView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, MemberOnly]
    @extend_schema(
        summary='그룹 참가자 리스트',
    )

    def get(self, request, study_group_id):
        study_group = get_object_or_404(StudyGroup, id=study_group_id)
        member = StudyMember.objects.filter(study_group=study_group)
        serializer = MemberSerializer(member, many=True)
        return response.Response(serializer.data)


class MemberDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        summary='그룹 탈퇴',
    )

    def delete(self, request, study_group_id):
        study_group = get_object_or_404(StudyGroup, id=study_group_id)
        user = request.user

        # 스터디 멤버 객체를 찾고 삭제
        try:
            member = StudyMember.objects.get(study_group=study_group, user=user)
            member.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except StudyMember.DoesNotExist:
            # 멤버가 존재하지 않는 경우
            return response.Response({'message': '해당 멤버가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)


class MemberUpdateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        summary='그룹장 위임',
        request=UpdateMemberSerializer,
    )

    def put(self, request, study_group_id):
        study_group = get_object_or_404(StudyGroup, id=study_group_id)
        request_user_member = get_object_or_404(StudyMember, study_group=study_group, user=request.user)
        target_user_id = request.data.get('user')

        # 요청한 사용자가 그룹장인지 확인
        if request_user_member.role != 1:
            return response.Response({'message': '오직 그룹장만이 권한이 있습니다.'}, status=status.HTTP_403_FORBIDDEN)

        with transaction.atomic():
            # 지정된 유저를 그룹장으로 설정
            target_user = get_object_or_404(User, id=target_user_id)
            target_member = get_object_or_404(StudyMember, study_group=study_group, user=target_user)
            target_member.role = 1
            target_member.save()

            # 요청한 사용자의 역할 변경 또는 삭제
            request_user_member.role = 0
            request_user_member.delete()  # 또는 request_user_member.save()를 사용하여 역할만 변경

        return response.Response({'message': 'Group leadership transferred successfully'}, status=status.HTTP_200_OK)