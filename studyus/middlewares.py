from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

class JWTAuthMiddleware(BaseMiddleware):
    """
    JWT 인증을 통한 사용자가 접근할 수 있습니다.
    """
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            await self.app(scope, receive, send)
        elif scope["type"] == "websocket":
            headers = scope.get("headers", [])
            token_list = [item[1] for item in headers if item[0] == b"sec-websocket-protocol"]
            if token_list:
                token = token_list[0].decode("utf-8")
                token = token.replace('ws-token, ', '')
            user = await self.get_user_from_token(token)
            scope["user"] = user
            print("미들 웨어에서 scope['user'] 담기 :: ", scope["user"])
            await self.app(scope, receive, send)
    
    @database_sync_to_async
    def get_user_from_token(self, token):
            try:
                # 토큰 검증 및 사용자 반환
                access_token = AccessToken(token)
                return User.objects.get(id=access_token.payload['user_id'])

            except Exception as e:
                # 토큰이 유효하지 않거나 사용자를 찾을 수 없는 경우
                return AnonymousUser()