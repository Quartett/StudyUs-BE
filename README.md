# Django_Final_Project 
# StudyUs
- 스터디원 모집 기능 및 실시간 채팅, 개인용 암기 플래시 카드 기능을 지원하는 웹 서비스입니다.

|Name|남영훈|오정배|윤재우|이수민|
|:-:|:-|:-|:-|:-|
| Profile  |-|-|-|-|
| Position |Frontend & Backend Develop & CICD|Frontend & Backend Develop & UIUX|Frontend & Backend Develop & UIUX|Frontend & Backend Develop & UIUX|
| GitHub |[Eric](https://github.com/Nam-Younghoon)|[OH_JUNGBAE](https://github.com/Alexmint001)|[bardnia](https://github.com/bardnia)|[su2minig](https://github.com/su2minig)|

## 목차

[1. 목표](#1-목표)<br>
[2. 개발 환경 및 배포 링크](#2-개발-환경-및-배포-링크)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도](#4-요구사항-시각화,-데이터베이스-모델링(ERD),-배포-아키텍처-구성도)<br>
[5. UI](#5-UI)<br>
[6. 메인 기능](#6-메인-기능)<br>
[7. 추가 기능](#7-추가-기능)<br>
[8. 개발하며 경험한 오류와 해결방법](#8-개발하며-경험한-오류와-해결방법)<br>
[9. 프로젝트 소감(어려웠던 점 & 배운 점)](#9-프로젝트-소감(어려웠던-점-&-배운-점))<br>
<br>

## 1. 목표
- #### 스터디 모집 또는 참여가 가능한 서비스
- #### 실시간 채팅 기능을 통해 소통 가능한 서비스
- #### 암기 플래시 카드 기능을 이용한 개인 학습 서비스

<br>

## 2. 개발 환경 및 배포 링크

### 2.1 개발 기술
#### [FrontEnd]  
<div>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
    <img src="https://img.shields.io/badge/Bootstrapap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/>
</div>

#### [BackEnd]
<div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
    <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>
</div>

#### [DataBase]
<div>
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/>
</div>

### 2.2 개발 환경 및 버전 관리
<div>
    <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</div>


<br>

### 2.2 배포 Link<br>
- #### [StudyUs-FE](https://studyus.kro.kr/)
<details>
<summary>테스트용 ID 및 PW</summary>
<div markdown="1">
ID : quarttet581@gmail.com<br>
PW : testpw581
</div>
</details>

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조
📦StudyUs-BE  
 ┣ 📂.git  
 ┣ 📂.github  
 ┣ 📂.vscode  
 ┣ 📂accounts  
 ┃ ┣ 📂management  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜adapters.py  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂chat  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜consumers.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜routing.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂media  
 ┃ ┗ 📂profile_images  
 ┣ 📂memorycard  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜permissions.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂study  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜permissions.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂studyus  
 ┣ 📂templates  
 ┃ ┗ 📂account  
 ┃ ┃ ┗ 📂email  
 ┃ ┃ ┃ ┣ 📜email_confirmation_message.html  
 ┃ ┃ ┃ ┣ 📜email_confirmation_signup_message.html  
 ┃ ┃ ┃ ┣ 📜email_confirmation_subject.txt  
 ┃ ┃ ┃ ┣ 📜login_fail.html  
 ┃ ┃ ┃ ┗ 📜login_success.html  
 ┣ 📂venv  
 ┣ 📜.env.dev  
 ┣ 📜.env.prod  
 ┣ 📜.gitignore  
 ┣ 📜manage.py  
 ┣ 📜README.md  
 ┗ 📜requirements.txt  
 
<br>

### 3.2 API 명세서
[StudyUs-Swagger](https://api-studyus.kro.kr/api/schema/swagger-ui/#/)

#### accounts

|App|URL|HTTP Method|HTML File Name|Note|Login|
|:-:|:-|:-:|:-|:-:|:-:|
|accounts|join/|POST|join.html|회원가입|-|
|accounts|login/|POST|login.html|로그인|-|
|accounts|user/|GET|profile.html|프로필 조회|O|
|accounts|user/|PATCH|profile_edit.html|프로필 수정|O|
|accounts|user/delete/|DELETE|-|회원 탈퇴|O|
|accounts|token/verify/|POST|-|토큰 유효성 검증|O|
|accounts|token/refresh/|POST|-|토큰 재발급|O|
|accounts|account-confirm-email/|POST|-|인증 메일 발송|-|
|accounts|account-confirm-email/{key}/|GET|-|이메일 인증|-|
|accounts|account/resend-email/|POST|-|인증 메일 재발송|-|
|accounts|password/change/|POST|change_password.html|비밀번호 변경|O|

#### study

|App|URL|HTTP Method|HTML File Name|Note|Login|Author|Member|
|:-:|:-|:-:|:-|:-:|:-:|:-:|:-:|
|study|create/|POST|studygroup_create.html|스터디그룹 생성|O|-|-|
|study|join/|POST|-|스터디그룹 참가|O|-|-|
|study|/|GET|index.html|스터디그룹 리스트 조회|-|-|-|
|study|{id}/|GET|studygroup_detail.html|스터디그룹 상세 조회|-|-|-|
|study|{id}/update/|PATCH|studygroup_edit.html|스터디그룹 수정|O|O|O|
|study|{id}/delete/|DELETE|-|스터디 그룹 삭제|O|O|O|
|study|{id}/member/|GET|-|스터디그룹 멤버 리스트 조회|-|-|-|
|study|{id}/member/delete/|DELETE|-|스터디그룹 탈퇴|O|-|O|
|study|{id}/member/update/|PATCH|-|스터디그룹 그룹장 위임|O|O|O|
|study|{id}/comments/|POST|-|댓글 작성|O|-|-|
|study|{id}/comments/|GET|-|댓글 리스트 조회|-|-|-|
|study|{id}/comments/{id}/update/|PATCH|-|댓글 수정|O|O|-|
|study|{id}/comments/{id}/delete/|DELETE|-|댓글 삭제|O|O|-|

#### memorycard

|App|URL|HTTP Method|HTML File Name|Note|Login|
|:-:|:-|:-:|:-:|:-|:-:|
|memorycard|/|GET|memorycard.html|암기 카드 전체 리스트 조회|O|
|memorycard|/|POST|-|암기 카드 생성|O|
|memorycard|{id}/|GET|memorycard_detail.html|암기 카드 상세 내역 조회|O|
|memorycard|{id}/|PATCH|-|암기 카드 수정|O|
|memorycard|{id}/|DELETE|-|암기 카드 삭제|O|
|memorycard|subject/|GET|subject.html|암기 카드 주제 리스트 조회|O|
|memorycard|subject/|POST|-|암기 카드 주제 리스트 생성|O|
|memorycard|subject/{id}/|GET|-|암기 카드 주제 상세 조회|O|
|memorycard|subject/{id}/|DELETE|-|암기 카드 주제 삭제|O|

### 3.3 개발 일정

<div align="center">
<img width="800" alt="NotionTimeline" src=""><br>
- 타임라인 - 이미지 수정 필요<br>
<br>

<img width="800" alt="WBS" src=""><br>
[WBS 스프레드시트](#)
이미지 수정 및 링크 수정 필요
</div>
<br>

## 4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도

<div align="center">
<img width="800" alt="MindMap" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/ec3bade0-cf47-41d2-81fe-1954bf62b854"><br>
    - 기능 요구사항(마인드맵)<br>
<br>

<img width="100%" alt="FlowChart" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/80893502-47a1-42e5-b946-91cbadfc2455"><br>
    - 플로우 차트<br>
<br>

<img width="800" alt="ERD" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/daebae1d-32a2-490a-83b3-b4ed5e33fbd5"><br>
    - 데이터베이스 모델링(ERD 설계)<br>
<br>

<img width="800" alt="architecture" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/75262393-7a93-4a04-b5b9-cc5c9c5f062e"><br>
    - 배포 아키텍처 구성도<br>
<br>
</div>
<br>

## 5. UI

### 5.1. 와이어프레임
<div align="center">
    
|||
|:-:|:-:|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/889b698c-9e5b-4e23-b1dc-ec55a2eab19c">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/edd0120c-49d7-4aea-8488-4b68c52690ab">|
|01. 로그인 페이지|02. 회원가입 페이지|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/80202635-53f5-424b-8fdb-46c07832bc77">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/127cc607-2708-49ee-b9ae-d4e961b2a6ab">|
|03. 프로필 페이지|04. 프로필 수정 페이지|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/53953777-8624-47d9-ab5c-b879f66eba84">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/d3e0f9eb-fb5a-4bc8-af85-122e3b270de7">|
|05. 비밀번호 변경 페이지|06. 메인 페이지 (로그인 전)|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/51fa4b42-b887-4422-b295-7af01a80f2c9">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/03540fed-26ff-4760-8fa6-867d0a8faf88">|
|07. 메인 페이지 (로그인 후)|08. 스터디 생성 페이지|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/42c48973-dc72-4ccb-a688-dcb5ef822660">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/a0dafa28-3c3c-4efa-b30c-8810b3484b2e">|
|09. 스터디 상세 페이지(스터디 멤버 X + 비로그인)|10. 스터디 상세 페이지(스터디 멤버O)|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/89a77b6d-f82e-48c0-ba37-bcc8aeadb595">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/42412224-1ca5-4406-9472-42936bdff11c">|
|11. 스터디 상세 페이지(스터디그룹장)|12. 스터디 수정 페이지|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/e51a18ba-0ac0-4cd3-818a-a25e88708485">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/cfc635df-5632-4ed0-bbef-408c90f0151c">|
|13. 실시간 채팅 페이지|14. 암기 카드 목록 페이지(주제 X)|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/879141ba-c9a0-4506-b47c-74fcb5bd7e22">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/e628d570-9aa1-4254-a244-073c728a671d">|
|15. 암기 카드 목록 페이지(주제 O)|16. 암기 카드 주제 작성 페이지|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/4cef97d5-1c18-4346-832b-1c132d554c23">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/007bd1fb-b4fe-4eaa-9332-9e1d4c0c533c">|
|17. 암기 카드 목록 페이지(카드 X)|18. 암기 카드 목록 페이지(카드  O)|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/e6d4f893-bf70-4caa-966d-3e5e3cf260fb">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/faebc0cc-ff9d-405c-8b71-a4a7374b96ba">|
|19. 암기 카드 작성 페이지|20. 암기 카드 수정 페이지|
|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/03923f8b-06d9-404f-880e-209f5fbd4b53">|<img width="700px" alt="image" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/a9d9fba9-ffe0-4f2c-a788-27f5bc017284">|
|21. 암기 카드 재생 페이지|22. 암기 카드 중요 표시 페이지|

</div>

### 5.2. 실제 UI
- GitHub Link : [StudyUs-FE](https://github.com/Quartett/StudyUs-FE)

## 6. 메인 기능
### 6.1. APP : accounts
#### 6.1.1. 회원 가입 시 이메일을 입력받고, 해당 이메일로 인증 메일을 받아 메일 내 링크 클릭 시 회원가입이 완료됨
- User 커스텀 모델 및 setting을 통해서 username을 사용하지 않고, email을 사용하였음.
    ```python
    # accounts/models.py
    class StudyUsUser(AbstractBaseUser):
    ...생략...
    email = models.EmailField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    ...생략...
    ```
    ```python
    # settings.py
    ...생략...
    AUTH_USER_MODEL = "accounts.StudyUsUser"
    ...생략...
    ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None # 사용자 이름 필드 지정
    ...생략...
    ```
    #### [⬆️ accounts/models.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/accounts/models.py#L6C1-L64C38)
- 이메일 인증의 경우 settings에서 all_auth 설정 및 view에서 ConfirmEmailView를 통해 구현하였음.
    ```python
    # settings.py
    ...생략...
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = env('EMAIL_HOST_USER') # 가입 인증 메일을 보낼 이메일
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') # 비밀번호(구글에서 앱 비밀번호 발급 필요)
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
    EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
    ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
    ACCOUNT_EMAIL_SUBJECT_PREFIX = '[studyus]'
    ...생략...
    ```
    #### [⬆️ settings.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/studyus/settings.py#L234C1-L247C43)
    ```python
    # accounts/views.py
    class ConfirmEmailView(APIView):
    ...생략...
    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        return render(self.request, 'account/email/login_success.html')

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                return render(self.request, 'account/email/login_fail.html')# 인증실패
        return email_confirmation
    ...생략...
    ```
    #### [⬆️ accounts/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/accounts/views.py#L18C1-L43C1)
- urls.py에서 repath와 정규 표현식을 통해 이메일 인증 key를 받는 url을 작성하였음.
    ```python
    accounts/urls.py
    urlpatterns = [
        ...생략...
        re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
        re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
        ...생략...
    ]
    ```
    #### [⬆️ accounts/urls.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/accounts/urls.py#L11C1-L12C117)
  
### 6.1.2. 인증 메일을 받지 못하였을 경우 재발송 버튼을 통해 인증 메일을 다시 요청하는 것이 가능
- urls.py에서 dj_rest_auth.registration의 기본 기능을 사용하여 인증 메일 재발송을 구현하였음.
    ```python
    # accounts/urls.py
    urlpatterns = [
        ...생략...
        path('account/', include('dj_rest_auth.registration.urls')),
        ...생략...
    ]
    ```
    #### [⬆️ accounts/urls.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/accounts/urls.py#L7C5-L7C65)
  
### 6.2. APP : study
#### 6.2.1. 스터디 그룹에 가입하고 싶을 경우 기존 스터디 그룹에서 가입 가능함
- models.py에서 max_members 필드를 작성하여 최대 인원을 정하고, views.py에서 JoinMemberView에서 post 요청이 들어왔을 때 현재 스터디 그룹의 멤버 수를 확인하고 max_members를 초과하면 가입을 못하고, 그보다 적을 경우 요청한 유저를 해당 그룹에 작성합니다.
    ```python
    # study/models.py
    class StudyGroup(models.Model):
        ...생략...
        max_members = models.IntegerField()
        ...생략...
    
    class StudyMember(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
        study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='study_group')
        role = models.IntegerField(default=0)
    ...생략...
    ```
    #### [⬆️ study/models.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/study/models.py#L10C1-L61C73)
    ```python
    # study/views.py
    class JoinMemberView(views.APIView):
    ...생략...
        def post(self, request):
            ...생략...
            if serializer.is_valid():
                ...생략...
                current_member_count = StudyMember.objects.filter(study_group=study_group).count()
    
                if current_member_count >= study_group.max_members:
                    return response.Response({'message': '멤버 수가 가득 찼습니다.'}, status=status.HTTP_400_BAD_REQUEST)
                member, created = StudyMember.objects.get_or_create(study_group=study_group, user=request.user, role=role)
    ...생략...
    ```
    #### [⬆️ study/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/study/views.py#L143C1-L167C69)

#### 6.2.2. 스터디 그룹을 생성하고 싶을 경우 필요한 정보 (스터디 그룹 명, 카테고리, 난이도, 일정 등)을 입력 받아 생성
- models.py에서 StudyGroup에 작성한 필드를 입력 받아 views.py의 StudygroupCreateView를 통해 post 요청이 들어오면 생성이 됩니다.
    ```python
    # study/models.py
    class Category(models.Model):
        category_name = models.CharField()
    
    
    class StudyGroup(models.Model):
    
        class Difficultys(models.IntegerChoices):
        ...생략...
    
        class Weeks(models.IntegerChoices):
        ...생략...
        
        thumbnail = models.ImageField(upload_to = 'study_images/', blank=True)
        title = models.TextField()
        level = models.IntegerField(choices=Difficultys.choices, default=Difficultys.EASY)
        week_days = models.TextField(default='', blank=True)
        content = models.TextField()
        ...생략...
        max_members = models.IntegerField()
        category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True, null=True)
        ...생략...
    ```
    #### [⬆️ study/models.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/study/models.py#L10C1-L49C26)
    ```python
    class StudygroupCreateView(generics.CreateAPIView):
        queryset = StudyGroup.objects.all()
        serializer_class = StudyGroupSerializer
        ...생략...
        
        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
        
        def perform_create(self, serializer):
            serializer.save()
            ChatRoom.objects.create(study_group=serializer.instance)
            StudyMember.objects.create(user=self.request.user, study_group=serializer.instance, role=1)
    ```
    #### [⬆️ study/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/study/views.py#L35C1-L50C100)
  
#### 6.2.3. 스터디 그룹의 멤버가 아니더라도 궁금한 것은 물어볼 수 있도록 그룹 내에서 댓글 작성이 가능합니다.
- views의 CommentCreateView를 통해 댓글을 작성하며 permission을 IsAuthenticated를 적용하여 로그인한 유저라면 댓글 작성이 가능하도록 하였습니다.
    ```python
    class CommentCreateView(generics.CreateAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer
        permission_classes = [permissions.IsAuthenticated]
    
        def perform_create(self, serializer):
            serializer.save(author=self.request.user)
    ```
    #### [⬆️ study/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/a4c5149aac0380d89d73febc7d3c1014239aad73/study/views.py#L99C1-L106C1)
  
#### 6.2.4. 스터디 그룹을 생성한 그룹장일 경우에만 그룹 정보 수정이 가능합니다.
- views의 StudygroupUpdateAPIView를 통해서 수정하며, permission을 MemberOnly로 적용함

### 6.3. APP : chat

#### 6.3.1. 스터디 그룹 내에서 멤버들끼리 실시간 채팅이 가능합니다.

### 6.4. APP : memorycard

#### 6.4.1. 로그인한 사용자 별로 암기용 플래시 카드를 주제 별로 작성 및 실헹하여 암기 공부에 도움을 받을 수 있습니다.

<br>

## 7. 추가 기능
### 7.1. 프로필 페이지 내에서 프로필 수정(프로필 이미지, 닉네임), 비밀번호 변경 및 회원 탈퇴가 가능합니다.
### 7.2. 스터디 그룹을 카테고리 별로 검색이 가능합니다.
### 7.3. 스터디 그룹의 그룹장을 변경할 수 있습니다.

<br>

## 8. 개발하며 경험한 오류와 해결방법

<br>

## 9. 프로젝트 소감(어려웠던 점 & 배운 점)
