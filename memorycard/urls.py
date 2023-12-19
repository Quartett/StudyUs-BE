from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, MemoryCardViewSet

router = DefaultRouter()
router.register(r'card', MemoryCardViewSet)
router.register(r'subject', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]