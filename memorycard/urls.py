from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemoryCardViewSet

router = DefaultRouter()
router.register('', MemoryCardViewSet, basename='memorycard')

urlpatterns = [
    path('', include(router.urls))
]