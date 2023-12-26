# test를 위한 모듈
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

# user model
from django.contrib.auth import get_user_model


class MemorycardTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        user = get_user_model().objects.create_user(
            email="test@test.com",
            nickname="테스트계정",
            password="lol123123"
        )
        refresh = RefreshToken.for_user(user=user)
        cls.access = refresh.access_token

    def setUp(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access}'
        )
        self.subject = {
            "title": "test_subject"
        }

        self.memorycard = {
            "memory_question": "test_question",
            "memory_answer": "test_answer",
            "bookmark": False,
            "difficulty": 1,
        }

    def test_create_subject(self):
        print("---주제 생성 테스트 시작---")
        response_create_subject = self.client.post(
            "/memorycard/subject/",
            data=self.subject
        )

        self.assertEqual(response_create_subject.status_code, 201)
        self.assertEqual(response_create_subject.data["title"], self.subject["title"])
        print("---주제 생성 테스트 성공---")
        print("---주제 생성 테스트 종료---")

    def test_delete_subject(self):
        print("---주제 삭제 테스트 시작---")
        response_create_subject = self.client.post(
            "/memorycard/subject/",
            data=self.subject
        )

        self.assertEqual(response_create_subject.status_code, 201)
        self.assertEqual(response_create_subject.data["title"], self.subject["title"])

        response_delete_subject = self.client.delete(
            f"/memorycard/subject/{response_create_subject.data["id"]}/"
        )

        self.assertEqual(response_delete_subject.status_code, 204)
        print("---주제 삭제 테스트 성공---")
        print("---주제 삭제 테스트 종료---")

    def test_create_memorycard(self):
        print("---암기카드 생성 테스트 시작---")
        response = self.client.post(
            "/memorycard/subject/",
            data=self.subject
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], self.subject["title"])

        self.memorycard["subject"] = response.data["id"]
        response = self.client.post(
            "/memorycard/",
            data=self.memorycard
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["memory_question"], self.memorycard["memory_question"])
        self.assertEqual(response.data["memory_answer"], self.memorycard["memory_answer"])
        self.assertEqual(response.data["bookmark"], self.memorycard["bookmark"])
        self.assertEqual(response.data["difficulty"], self.memorycard["difficulty"])
        print("---암기카드 생성 테스트 성공---")
        print("---암기카드 생성 테스트 종료---")

    def test_delete_memorycard(self):
        print("---암기카드 삭제 테스트 시작---")
        response_create_subject = self.client.post(
            "/memorycard/subject/",
            data=self.subject
        )

        self.assertEqual(response_create_subject.status_code, 201)
        self.assertEqual(response_create_subject.data["title"], self.subject["title"])

        self.memorycard["subject"] = response_create_subject.data["id"]
        response_create_memorycard = self.client.post(
            "/memorycard/",
            data=self.memorycard
        )

        self.assertEqual(response_create_memorycard.status_code, 201)

        response_delete_memorycard = self.client.delete(
            f"/memorycard/{response_create_memorycard.data['id']}/"
        )

        self.assertEqual(response_delete_memorycard.status_code, 204)
        print("---암기카드 삭제 테스트 성공---")
        print("---암기카드 삭제 테스트 종료---")

    def test_patch_memorycard(self):
        print("---암기카드 수정 테스트 시작---")
        response_create_subject = self.client.post(
            "/memorycard/subject/",
            data=self.subject
        )

        self.assertEqual(response_create_subject.status_code, 201)
        self.assertEqual(response_create_subject.data["title"], self.subject["title"])

        self.memorycard["subject"] = response_create_subject.data["id"]
        response_create_memorycard = self.client.post(
            "/memorycard/",
            data=self.memorycard
        )

        self.assertEqual(response_create_memorycard.status_code, 201)

        response_patch_memorycard = self.client.patch(
            f"/memorycard/{response_create_memorycard.data['id']}/",
            data={"memory_question": "updated_question"}
        )

        self.assertEqual(response_patch_memorycard.status_code, 200)
        self.assertEqual(response_patch_memorycard.data["memory_question"], "updated_question")
        print("---암기카드 수정 테스트 성공---")
        print("---암기카드 수정 테스트 종료---")
