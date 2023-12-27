# test를 위한 모듈
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

# user model
from django.contrib.auth import get_user_model
from .models import Category

class StudyTest(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        user = get_user_model().objects.create_user(
            email="test@test.com",
            nickname="테스트계정",
            password="sumin1234"
        )
        refresh = RefreshToken.for_user(user=user)
        cls.access = refresh.access_token

        Category.objects.create(
            category_name="테스트 카테고리"
        )
        print("카테고리", Category.objects.all())

    def setUp(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access}"
        )
        self.studygroup = {
            "title": "테스트 스터디",
            "level": 1,
            "week_days": "월,화,수,목,금",
            "category": 1,
            "content": "테스트 스터디 내용",
            "study_start_at": "2023-12-27",
            "study_end_at": "2023-12-29",
            "max_members": 5,
        }
        self.comment = {
            "study_group": 1,
            "text": "테스트 댓글"
        }

    def test_create_studygroup(self):
        print("---스터디그룹 생성 테스트 시작---")
        response_create_studygroup = self.client.post(
            "/study/create/",
            data = self.studygroup
        )

        self.assertEqual(response_create_studygroup.status_code, 201)
        self.assertEqual(response_create_studygroup.data["title"], self.studygroup["title"])
        print("---스터디그룹 생성 테스트 성공---")
        print("---스터디그룹 생성 테스트 종료---")

    def test_patch_studygroup(self):
        print("---스터디그룹 수정 테스트 시작---")
        response_create_studygroup = self.client.post(
            "/study/create/",
            data = self.studygroup
        )

        self.assertEqual(response_create_studygroup.status_code, 201)
        self.assertEqual(response_create_studygroup.data["title"], self.studygroup["title"])

        response_patch_studygroup = self.client.patch(
            f"/study/{response_create_studygroup.data["id"]}/update/",
            data = {
                "title": "테스트 스터디 수정"
            }
        )

        self.assertEqual(response_patch_studygroup.status_code, 200)
        self.assertEqual(response_patch_studygroup.data["title"], "테스트 스터디 수정")
        print("---스터디그룹 수정 테스트 성공---")
        print("---스터디그룹 수정 테스트 종료---")

    def test_delete_studygroup(self):
        print("---스터디그룹 삭제 테스트 시작---")
        response_create_studygroup = self.client.post(
            "/study/create/",
            data = self.studygroup
        )

        self.assertEqual(response_create_studygroup.status_code, 201)
        self.assertEqual(response_create_studygroup.data["title"], self.studygroup["title"])

        response_delete_studygroup = self.client.delete(
            f"/study/{response_create_studygroup.data["id"]}/delete/"
        )

        self.assertEqual(response_delete_studygroup.status_code, 204)
        print("---스터디그룹 삭제 테스트 성공---")
        print("---스터디그룹 삭제 테스트 종료---")

    def test_create_comment(self):
        print("---댓글 생성 테스트 시작---")
        response_create_studygroup = self.client.post(
            "/study/create/",
            data = self.studygroup
        )

        self.assertEqual(response_create_studygroup.status_code, 201)
        self.assertEqual(response_create_studygroup.data["title"], self.studygroup["title"])

        response_create_comment = self.client.post(
            "/study/comments/",
            data = {
                "study_group": response_create_studygroup.data["id"],
                "text": "테스트 댓글"
            }
        )

        self.assertEqual(response_create_comment.status_code, 201)
        self.assertEqual(response_create_comment.data["text"], self.comment["text"])
        print("---댓글 생성 테스트 성공---")
        print("---댓글 생성 테스트 종료---")
    
    def test_patch_comment(self):
        print("---댓글 수정 테스트 시작---")
        response_create_studygroup = self.client.post(
            "/study/create/",
            data = self.studygroup
        )

        self.assertEqual(response_create_studygroup.status_code, 201)
        self.assertEqual(response_create_studygroup.data["title"], self.studygroup["title"])

        response_create_comment = self.client.post(
            "/study/comments/",
            data = {
                "study_group": response_create_studygroup.data["id"],
                "text": "테스트 댓글"
            }
        )

        self.assertEqual(response_create_comment.status_code, 201)
        self.assertEqual(response_create_comment.data["text"], self.comment["text"])

        response_patch_comment = self.client.patch(
            f"/study/comments/{response_create_comment.data["id"]}/update/",
            data = {
                "text": "테스트 댓글 수정"
            }
        )

        self.assertEqual(response_patch_comment.status_code, 200)
        self.assertEqual(response_patch_comment.data["text"], "테스트 댓글 수정")
        print("---댓글 수정 테스트 성공---")
        print("---댓글 수정 테스트 종료---")

    def test_delete_comment(self):
        print("---댓글 삭제 테스트 시작---")
        response_create_studygroup = self.client.post(
            "/study/create/",
            data = self.studygroup
        )

        self.assertEqual(response_create_studygroup.status_code, 201)
        self.assertEqual(response_create_studygroup.data["title"], self.studygroup["title"])

        response_create_comment = self.client.post(
            "/study/comments/",
            data = {
                "study_group": response_create_studygroup.data["id"],
                "text": "테스트 댓글"
            }
        )

        self.assertEqual(response_create_comment.status_code, 201)
        self.assertEqual(response_create_comment.data["text"], self.comment["text"])

        response_delete_comment = self.client.delete(
            f"/study/comments/{response_create_comment.data["id"]}/delete/"
        )

        self.assertEqual(response_delete_comment.status_code, 204)
        print("---댓글 삭제 테스트 성공---")
        print("---댓글 삭제 테스트 종료---")