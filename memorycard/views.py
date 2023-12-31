from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from .models import Subject, MemoryCard
from .serializers import SubjectSerializer, MemoryCardSerailizer
from .permissions import IsOwnerOrReadOnly
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from django.db import IntegrityError

@extend_schema_view(
    update = extend_schema(
        exclude=True
    ),
    partial_update = extend_schema(
        exclude=True
    ),
    list = extend_schema(
        summary="암기 카드 Subject 리스트",
        description="사용자가 생성한 암기 카드 Subject 리스트"
    ),
    create = extend_schema(
        summary="암기 카드 Subject 생성",
        description="암기 카드의 Subject를 생성합니다"
    ),
    destroy = extend_schema(
        summary="암기 카드 Subject 삭제",
        description="암기 카드의 Subject를 삭제합니다"
    ),
    retrieve = extend_schema(
        summary="암기 카드 Subject 상세내용",
        description="암기 카드의 Subject 상세 내용입니다"
    ),
)
class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            error_message = {
                "detail": "이미 존재하는 주제입니다."
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema_view(
    update = extend_schema(
        exclude=True
    ),
    partial_update = extend_schema(
        summary="암기 카드 수정",
        description="암기 카드를 수정합니다"
    ),
    list = extend_schema(
        summary="암기 카드 전체 리스트",
        description="사용자가 생성한 암기 카드 전체 리스트",
        parameters=[
            OpenApiParameter(
                name="subject",
                type=int, 
                description="주제 아이디를 입력하여 해당 암기카드들만 필터링", 
                required=False)
        ]
    ),
    create = extend_schema(
        summary="암기 카드 생성",
        description="암기 카드를 생성합니다"
    ),
    destroy = extend_schema(
        summary="암기 카드 삭제",
        description="암기 카드를 삭제합니다"
    ),
    retrieve = extend_schema(
        summary="암기 카드 상세내역",
        description="암기 카드의 상세 내역입니다"
    ),
)
class MemoryCardViewSet(ModelViewSet):
    queryset = MemoryCard.objects.all()
    serializer_class = MemoryCardSerailizer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        subject = self.request.GET.get('subject', '')
        bookmark = self.request.GET.get('bookmark', 'off')
        
        if subject and bookmark == 'on':
            return self.queryset.filter(subject__user=self.request.user, subject__id=subject, bookmark=True)
        elif subject and bookmark == "off":
            return self.queryset.filter(subject__user=self.request.user, subject__id=subject)
        return self.queryset.filter(subject__user=self.request.user)
    
    def perform_create(self, serializer):
        subject_id = self.request.data.get('subject')
        serializer.save(subject=get_object_or_404(Subject, pk=subject_id))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        next_memorycard = MemoryCard.objects.filter(subject=instance.subject, id__gt=instance.id).order_by('id').first()
        prev_memorycard = MemoryCard.objects.filter(subject=instance.subject, id__lt=instance.id).order_by('-id').first()
        data = {
            "data": serializer.data,
            "next_memorycard_id": next_memorycard.id if next_memorycard else None,
            "prev_memorycard_id": prev_memorycard.id if prev_memorycard else None
        }

        return Response(data)
