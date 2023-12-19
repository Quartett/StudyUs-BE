from django.urls import path, re_path, include
from .views import ConfirmEmailView, UserDeleteView
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('join/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    # path('user/change_status/', UserStatusView.as_view(), name='chang_user_status'),
    path('user/delete/', UserDeleteView.as_view(), name='user_delete'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
]