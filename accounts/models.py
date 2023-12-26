from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.text import slugify

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
    
    def create_superuser(self, email, password):
        user = self.model(
            email = self.normalize_email(email),
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class StudyUsUser(AbstractBaseUser, PermissionsMixin):
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile.svg')
    nickname = models.CharField(max_length=20, unique=True, blank=True) 
    email = models.EmailField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    
    objects = StudyUsUserManager()

    date_joined = models.DateTimeField(auto_now_add=True)
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
    
    def save(self, *args, **kwargs):
        '''
        닉네임이 없을 경우 이메일의 앞부분을 닉네임으로 사용
        '''
        if not self.nickname and self.email:
            self.nickname = slugify(self.email.split('@')[0])[:20]
        super().save(*args, **kwargs)