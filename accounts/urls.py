from django.urls import path
from .views import UserDeleteView

urlpatterns = [
    path('user/delete/', UserDeleteView.as_view(), name='user_delete'),
]