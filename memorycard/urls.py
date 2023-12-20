from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, MemoryCardViewSet

router = DefaultRouter()
router.register(r'subject', SubjectViewSet, basename="memorycard")
router.register(r'', MemoryCardViewSet, basename="memorycard")

urlpatterns = [
    path('', include(router.urls)),
]