import os, django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from .middlewares import JWTAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studyus.settings")
django.setup()

from chat.routing import websocket_urlpatterns

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(URLRouter(websocket_urlpatterns))
    )
})
