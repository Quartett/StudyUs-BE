from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # API 스키마 제공(yaml파일)
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # 테스트할 수 있는 UI
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # API 문서화를 위한 UI
    path('accounts/', include('accounts.urls')),
    path('study/', include('study.urls'),),
    path('memorycard/', include('memorycard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)