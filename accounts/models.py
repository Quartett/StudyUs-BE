from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class StudyUsUserManager(BaseUserManager):
    
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nickname, password):
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class StudyUsUser(AbstractBaseUser, PermissionsMixin):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    
    objects = StudyUsUserManager()

    date_joined = models.DateTimeField(auto_now_add=True)
    # last_login은 AbstractBaseUser에 존재
    
    # permission
    is_superuser = models.BooleanField(default=False) # 최상위 권한 - 슈퍼유저
    is_admin = models.BooleanField(default=False) # 차상위 권한 - 관리자
    is_staff = models.BooleanField(default=False) # 상위 권한 - 운영자
    is_active = models.BooleanField(default=True) # 활성화 여부
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser