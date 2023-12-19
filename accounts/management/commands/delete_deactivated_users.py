from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta

class Command(BaseCommand):
    help = 'Delete users that are deactivated for more than 5 days'

    def handle(self, *args, **options):
        User = get_user_model()
        # 현재 시간에서 5일 전의 시간을 계산
        time_threshold = timezone.now() - timedelta(days=5)

        # is_active가 False이고, last_login이 5일 이전인 사용자를 필터링
        users_to_delete = User.objects.filter(is_active=False, last_login__lt=time_threshold)

        # 필터링된 사용자를 삭제
        users_to_delete.delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted users'))
