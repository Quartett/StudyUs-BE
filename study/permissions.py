from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class MemberOnly(permissions.BasePermission):
    """
    해당 스터디 그룹의 멤버에게만 접근을 허용하는 권한 클래스
    """

    def has_permission(self, request, view):
        # URL에서 study_group_id를 추출
        study_group_id = view.kwargs.get('study_group_id')

        # study_group_id가 없다면 False 반환
        if not study_group_id:
            return False

        # StudyGroup 객체를 가져옴, 존재하지 않으면 404 에러
        study_group = get_object_or_404(StudyGroup, id=study_group_id)

        # 요청을 보낸 사용자가 해당 스터디 그룹의 멤버인지 확인
        return StudyMember.objects.filter(study_group=study_group, user=request.user).exists()