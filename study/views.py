from django.shortcuts import render
from rest_framework import generics, permissions
from .models import StudyGroup, Comment, Category
from .serializers import CommentSerializer, StudyGroupSerializer


class StudygroupListAPIView(generics.ListAPIView):
    # 목록
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

class StudygroupCreateView(generics.CreateAPIView):
    # 생성
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class StudygroupRetrieveAPIView(generics.RetrieveAPIView):
    # 상세조회
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

class StudygroupUpdateAPIView(generics.UpdateAPIView):
    # 업데이트
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer


class StudygroupDestroyAPIView(generics.DestroyAPIView):
    # 삭제
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

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])