from django.urls import path
from . import views


urlpatterns = [
    path('', views.StudygroupListAPIView.as_view(), name='studylist'),
    path('create/', views.StudygroupCreateView.as_view(), name='study'),
    path('<int:pk>/', views.StudygroupRetrieveAPIView.as_view(), name='studydetail'),
    path('<int:pk>/update/', views.StudygroupUpdateAPIView.as_view(), name='studyupdate'),
    path('<int:pk>/delete/', views.StudygroupDestroyAPIView.as_view(), name='studydelete'),
    # path('comment/', views.StudygroupCreateView.as_view(), name='study'),
    # path('comment/<int:pk>/', views.~~~, name='study'),
    # path('member/', views.~~~, name='study'),
    # path('change/master/', views.~~~, name='study'),
    # path('join/', views.~~~, name='study'),
]