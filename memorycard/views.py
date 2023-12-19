from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import MemoryCard
from .serializers import MemoryCardSerailizer
from drf_spectacular.utils import extend_schema_view, extend_schema

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
        description="사용자가 생성한 암기 카드 전체 리스트"
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)