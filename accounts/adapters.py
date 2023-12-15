from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        profile_image = data.get('profile_image')
        nickname = data.get('nickname')
        date_joined = data.get('date_joined')
        last_login = data.get('last_login')
        is_superuser = data.get('is_superuser')
        is_admin = data.get('is_admin')
        is_staff = data.get('is_staff')
        is_active = data.get('is_active')
        
        if profile_image:
            user.profile_image = profile_image
            
        if nickname:
            user.nickname = nickname
            
        if date_joined:
            user.date_joined = date_joined
            
        if last_login:
            user.last_login = last_login
            
        if is_superuser:
            user.is_superuser = is_superuser
            
        if is_admin:
            user.is_admin = is_admin
            
        if is_staff:
            user.is_staff = is_staff
            
        if is_active:
            user.is_active = is_active            
            
        user.save()
        return user