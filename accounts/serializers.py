from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer, UserDetailsSerializer as RestAuthUserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer

User = get_user_model()

class RegisterSerializer(RestAuthRegisterSerializer):
    username = None
    profile_image = serializers.ImageField(required=False)
    nickname = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ('profile_image', 'nickname', 'email', 'password1', 'password2')
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise DjangoValidationError('비밀번호가 일치하지 않습니다.')
        return data
    
    def get_cleaned_data(self):
        data = super(RegisterSerializer, self).get_cleaned_data()
        data['profile_image'] = self.validated_data.get('profile_image', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        return data
    
    def save(self, request):
        user = super().save(request)
        if user:
            user.profile_image = self.data.get('profile_image')
            user.nickname = self.data.get('nickname')
        user.save()
        return user

class LoginSerializer(RestAuthLoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
        
class UserDetailsSerializer(RestAuthUserDetailsSerializer):
    username = None
    class Meta:
        model = User
        fields = ('profile_image', 'nickname', 'email')
        read_only_fields = ('email', 'date_joined', 'last_login', 'is_superuser', 'is_admin', 'is_staff', 'is_active')
        
    def update(self, instance, validated_data):
        # meta.fields에 있는 필드만 업데이트
        update_fields = self.Meta.fields
        for field in update_fields:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))

        instance = super().update(instance, validated_data)
        return instance