# Django 모듈
from django.db import transaction
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Django 서드 파티 모듈
from rest_framework import generics, permissions, filters 
from rest_framework.response import Response
from chat.models import ChatRoom
from rest_framework import views, response, status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

# 내부 파일 또는 라이브러리
from .serializers import CommentSerializer, StudyGroupSerializer, MemberSerializer, UpdateMemberSerializer
from .models import StudyGroup, Comment, StudyMember
from .permissions import MemberOnly, IsOwnerOrReadOnly

User = get_user_model()

class StudygroupListAPIView(generics.ListAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'category__category_name']
    
    @extend_schema(
        summary='스터디그룹 리스트',
    )

    def get(self, request):
        return self.list(request)


class StudygroupCreateView(generics.CreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(
        summary='스터디그룹 생성',
    )
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save()
        ChatRoom.objects.create(study_group=serializer.instance)
        StudyMember.objects.create(user=self.request.user, study_group=serializer.instance, role=1)


class StudygroupRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

    @extend_schema(
        summary='스터디그룹 상세보기',
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudygroupUpdateAPIView(generics.UpdateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [MemberOnly]
    
    @extend_schema(
        summary='스터디그룹 수정하기',
    )
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    @extend_schema(
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class StudygroupDestroyAPIView(generics.DestroyAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated, MemberOnly]

    @extend_schema(
        summary='스터디그룹 삭제하기',
    )

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@extend_schema(
        summary='댓글 작성',
    )
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(
        summary='댓글 리스트',
    )
class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(study_group_id=self.kwargs['pk'])


@extend_schema(
    summary='댓글 업데이트',
)
class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    @extend_schema(
    exclude=True
)
    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(
    summary='댓글 삭제'
)
class CommentDestroyView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


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

            # 현재 스터디 그룹의 멤버 수를 확인합니다.
            current_member_count = StudyMember.objects.filter(study_group=study_group).count()

            # max_members를 초과하면 가입을 거부합니다.
            if current_member_count >= study_group.max_members:
                return response.Response({'message': '멤버 수가 가득 찼습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            member, created = StudyMember.objects.get_or_create(study_group=study_group, user=request.user, role=role)

            if not created:
                # 이미 참여중인 경우, 409 Conflict 반환
                return response.Response(status=status.HTTP_409_CONFLICT)
            return response.Response(status=status.HTTP_201_CREATED)


class MemberListView(views.APIView):
    @extend_schema(
        summary='그룹 참가자 리스트',
    )

    def get(self, request, pk):
        study_group = get_object_or_404(StudyGroup, id=pk)
        member = StudyMember.objects.filter(study_group=study_group)
        serializer = MemberSerializer(member, many=True)
        return response.Response(serializer.data)


class MemberDeleteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        summary='그룹 탈퇴',
    )

    def delete(self, request, pk):
        study_group = get_object_or_404(StudyGroup, id=pk)
        user = request.user

        try:
            member = StudyMember.objects.get(study_group=study_group, user=user)

            if member.role == 1:
                new_leader = StudyMember.objects.filter(
                    study_group=study_group
                ).exclude(
                    user=user
                ).first()

                if new_leader:
                    new_leader.role = 1
                    new_leader.save()
                else:
                    return response.Response(
                        {'message': '다른 멤버가 없으므로 그룹을 탈퇴할 수 없습니다.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # 현재 멤버 삭제
            member.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        except StudyMember.DoesNotExist:
            # 멤버가 존재하지 않는 경우
            return response.Response({'message': '해당 멤버가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)


class MemberUpdateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, MemberOnly]
    @extend_schema(
        summary='그룹장 위임',
        request=UpdateMemberSerializer,
    )

    def patch(self, request, pk):
        study_group = get_object_or_404(StudyGroup, id=pk)
        request_user_member = get_object_or_404(StudyMember, study_group=study_group, user=request.user)
        target_user_id = request.data.get('user')

        with transaction.atomic():
            # 지정된 유저를 그룹장으로 설정
            target_user = get_object_or_404(User, id=target_user_id)
            target_member = get_object_or_404(StudyMember, study_group=study_group, user=target_user)
            target_member.role = 1
            target_member.save()

            # 요청한 사용자의 역할 변경 또는 삭제
            request_user_member.role = 0
            request_user_member.save()

        return response.Response({'message': '그룹장 변경 성공'}, status=status.HTTP_200_OK)
