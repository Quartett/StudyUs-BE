from django.urls import path, re_path, include
from .views import ConfirmEmailView, UserDeleteView, CustomRegisterView
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('join/', CustomRegisterView.as_view(), name='rest_register'),
    path('allauth/', include('allauth.urls')),
    path('user/delete/', UserDeleteView.as_view(), name='user_delete'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
]