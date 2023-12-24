from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    작성자만 생성 가능하게 권한을 부여한다
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.subject.user == request.user