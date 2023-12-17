from dj_rest_auth.registration.views import RegisterView
from django.db import IntegrityError
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout
from .serializers import UserDetailsSerializer

User = get_user_model()

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


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        logout(request)
        
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('my-refresh-token')
        response.delete_cookie('my-access-token')
        return response
    
    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.pk)
    
    def get_object(self):
        return self.get_queryset().get()