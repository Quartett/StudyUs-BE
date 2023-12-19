from dj_rest_auth.registration.views import RegisterView
from django.db import IntegrityError
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout
from .serializers import UserDetailsSerializer
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

User = get_user_model()

class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]
    serializer_class = None # 사용하지 않음
    
    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        return HttpResponseRedirect('/login/success/') # 인증성공

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                return HttpResponseRedirect('/login/failure') # 인증실패
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs


class CustomRegisterView(RegisterView):

    def create(self, request, args, **kwargs):
        try:
            return super().create(request,args, **kwargs)
        except IntegrityError as e:
            error_message = "이미 가입된 이메일이거나 중복된 닉네임입니다."
            response_data = {
                "detail": error_message
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


# class UserStatusView(generics.RetrieveUpdateAPIView):
#     '''
#     사용자의 is_active 상태를 변경하는 API
#     is_active가 True일 경우 활성화 상태
#     is_active가 False일 경우 탈퇴 상태
#     '''
#     queryset = User.objects.all()
#     serializer_class = UserStatusSerializer
    
#     def patch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.is_active = request.data['is_active']
#         instance.save()
        
#         logout(request)
        
#         response = Response(status=status.HTTP_204_NO_CONTENT)
#         return response
    
#     def get_queryset(self):
#         return self.queryset.filter(pk=self.request.user.pk)
    
#     def get_object(self):
#         return self.get_queryset().get()
    
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        logout(request)
        
        response = Response(status=status.HTTP_204_NO_CONTENT)
        return response
    
    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.pk)
    
    def get_object(self):
        return self.get_queryset().get()