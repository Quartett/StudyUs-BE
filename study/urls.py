from django.urls import path
from . import views


urlpatterns = [
    path('', views.StudygroupListAPIView.as_view(), name='studylist'),
    path('create/', views.StudygroupCreateView.as_view(), name='study'),
    path('<int:pk>/', views.StudygroupRetrieveAPIView.as_view(), name='studydetail'),
    path('<int:pk>/update/', views.StudygroupUpdateAPIView.as_view(), name='studyupdate'),
    path('<int:pk>/delete/', views.StudygroupDestroyAPIView.as_view(), name='studydelete'),
    path('comments/', views.CommentCreateView.as_view(), name='comment-create'),
    # 댓글 리스트
    path('<int:pk>/comments/', views.CommentListView.as_view(), name='comment-list'),
    # 댓글 수정
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    # 댓글 삭제
    path('comments/<int:pk>/delete/', views.CommentDestroyView.as_view(), name='comment-delete'),
    # 그룹 참가
    path('join/', views.JoinMemberView.as_view(), name='group-join' ),
    # 그룹 참가자 리스트
    path('<int:pk>/member/', views.MemberListView.as_view(), name='group-member' ), 
    # 그룹 참가자 상세보기
    path('<int:pk>/member/delete', views.MemberDeleteView.as_view(), name='group-member-detail' ),
    # 그룹 참가자 업데이트
    path('<int:pk>/member/update', views.MemberUpdateView.as_view(), name='group-member-update' ),
]
