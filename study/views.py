from django.shortcuts import render
from rest_framework import generics, permissions
from .models import StudyGroup, Comment, Category
from chat.models import ChatRoom
from .serializers import CommentSerializer, StudyGroupSerializer


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

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])
