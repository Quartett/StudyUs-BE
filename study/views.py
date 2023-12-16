from django.shortcuts import render
from rest_framework import generics, permissions
from .models import StudyGroup, StudyMember, Comment
from .serializers import CommentSerializer, StudyGroupSerializer, StudyMemberSerializer


class StudygroupCreateView(generics.CreateAPIView):
    # 회원만 스터디 생성 가능
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudygroupListAPIView(generics.ListAPIView):
    # 비회원도 스터디 확인 가능
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class StudygroupRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # 스터디 확인과 수정, 삭제
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudyMemberCreateView(generics.CreateAPIView):
    # 스터디 맴버 생성
    queryset = StudyMember.objects.all()
    serializer_class = StudyMemberSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudyMemberRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    # 스터디 맴버 확인과 수정
    queryset = StudyMember.objects.all()
    serializer_class = StudyMemberSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StudyMemberRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    # 스터디 맴버 확인과 삭제
    queryset = StudyMember.objects.all()
    serializer_class = StudyMemberSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])