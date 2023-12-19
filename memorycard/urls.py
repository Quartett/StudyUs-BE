from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, MemoryCardViewSet

router = DefaultRouter()
router.register('memorycard', MemoryCardViewSet)
router.register('subject', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]