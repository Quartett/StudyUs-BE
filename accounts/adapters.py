from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        
        profile_image = data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        
        user.nickname = data.get('nickname', '')
        user.is_superuser = data.get('is_superuser', False)
        user.is_admin = data.get('is_admin', False)
        user.is_staff = data.get('is_staff', False)
        
        user.is_active = True
        
        user.save()
        
        return user