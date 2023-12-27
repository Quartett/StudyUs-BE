# Django_Final_Project 
# StudyUs
- 스터디원 모집 기능 및 실시간 채팅, 개인용 암기 플래시 카드 기능을 지원하는 웹 서비스입니다.

|Name|남영훈|오정배|윤재우|이수민|
|:-:|:-:|:-:|:-:|:-:|
| Profile  |<img width="150px" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/c0ff7054-39b1-42e5-a996-27471d41540d">|<img width="150px" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/8733be77-4d9c-42a1-a946-320c8644d785">|<img width="150px" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/d6583404-66a5-4c60-9345-c3d97527c733">|<img width="150px" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/a231294d-4391-4885-a580-8089adcfbf8d">|
| Position |Architect<br>Frontend Develop<br>Backend Develop<br>CICD|팀장<br>Frontend Develop<br>Backend Develop<br>UIUX|Frontend Develop<br>Backend Develop<br>기능 요구사항 분석|Frontend Develop<br>Backend Develop<br>UIUX<br>ERD, API 명세서 작성|
| GitHub |[Eric](https://github.com/Nam-Younghoon)|[OH_JUNGBAE](https://github.com/Alexmint001)|[bardnia](https://github.com/bardnia)|[su2minig](https://github.com/su2minig)|

## 목차

[1. 목표](#1-목표)<br>
[2. 개발 환경 및 배포 링크](#2-개발-환경-및-배포-링크)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도](#4-요구사항-시각화,-데이터베이스-모델링erd,-배포-아키텍처-구성도)<br>
[5. UI](#5-UI)<br>
[6. 메인 기능](#6-메인-기능)<br>
[7. 추가 기능](#7-추가-기능)<br>
[8. 개발하며 경험한 오류와 해결방법](#8-개발하며-경험한-오류와-해결방법)<br>
[9. 프로젝트 소감(어려웠던 점 & 배운 점)](#9-프로젝트-소감어려웠던-점--배운-점)<br>
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
    <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/>
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
<img width="800" alt="NotionTimeline" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/0e74f326-4882-466e-93e4-1714b287db04"><br>
    
타임라인

<br>


<img width="800" alt="WBS" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/ecd40f5c-abc4-42e8-856b-7de9087afce6"><br>
[WBS 스프레드시트](https://docs.google.com/spreadsheets/d/1K5nbBxawXs0l7qWXfOIy9vtu1i8Ugt9n5Vk12vMWqwI/edit?usp=sharing)
</div>
<br>

## 4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도
- 마인드 맵과 플로우 차트는 Figma로 작성되었습니다.
- ERD는 dbdiagram.io로 작성되었습니다.
<div align="center">
<img width="800" alt="MindMap" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/ec3bade0-cf47-41d2-81fe-1954bf62b854"><br>
    
[기능 요구사항(마인드맵)](https://www.figma.com/file/7g90jNTrXgVX7R2X5MOoph/Django-final-project-mind-map?type=whiteboard&node-id=0%3A1&t=NjyKkwH8OGcfUSHE-1)
    
    
<br>

<img width="100%" alt="FlowChart" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/80893502-47a1-42e5-b946-91cbadfc2455"><br>

[플로우 차트](https://www.figma.com/file/rMiTnkbJ4NA52qOVSs5rlf/Django-Final-Project-Flow-Chart?type=whiteboard&node-id=0%3A1&t=iPjp3b0S7fAAUhgc-1)
    
<br>

<img width="800" alt="ERD" src="https://github.com/Quartett/StudyUs-BE/assets/142385654/107f823b-7892-4543-a525-fa6cf822ab64"><br>

[데이터베이스 모델링(ERD 설계)](https://dbdiagram.io/d/StudyUs-6573add256d8064ca0ae01f1)
    
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
    <br>
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
    <br>
    
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
    <br>
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
    <br>
  
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
    <br>
  
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
    <br>
    
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
    <br>

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
    <br>
    
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
    <br>
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
    <br>
#### 6.2.4. 스터디 그룹을 생성한 그룹장일 경우에만 그룹 정보 수정이 가능합니다.
- views의 StudygroupUpdateAPIView를 통해서 수정하며, permission을 LeaderOnly로 적용하였습니다.
    ```python
    # study/views.py
    class StudygroupUpdateAPIView(generics.UpdateAPIView):
        queryset = StudyGroup.objects.all()
        serializer_class = StudyGroupSerializer
        permission_classes = [LeaderOnly]
        ...생략...
    ```
    #### [⬆️ study/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/3c09f74fcd957792ae28fcacc9178569835bcb41/study/views.py#L65C1-L81C67)
    <br>
- LeaderOnly는 요청의 종류에 따라 스터디그룹의 일반 멤버에게만 권한을 줄지, 스터디 그룹장에게만 권한을 줄지 설정하는 클래스입니다.
    ```python
    # study/permissions.py
    class LeaderOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        ...생략...
        if request.method in permissions.SAFE_METHODS:
            return StudyMember.objects.filter(study_group=study_group, user=request.user).exists()
        return StudyMember.objects.filter(study_group=study_group, user=request.user, role=1).exists()
        ...생략...
    ```
    #### [⬆️ study/permissions.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/3c09f74fcd957792ae28fcacc9178569835bcb41/study/permissions.py#L5C1-L26C20)
    <br>

### 6.3. APP : memorycard

#### 6.3.1. 로그인한 사용자 별로 암기용 플래시 카드를 주제 별로 작성 및 실헹하여 암기 공부에 도움을 받을 수 있습니다.
- models.py에 Subject와 MemoryCard를 작성하고 1:N 관계로 적용함(ForiegnKey)으로써 하나의 Subject가 여러개의 MemoryCard를 가질 수 있도록 하였습니다.
    ```python
    # memorycard/models.py
    class Subject(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=50)
        ...생략...    
            
    class MemoryCard(models.Model):
        ...생략...
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        ...생략...
    ```
    #### [⬆️ memorycard/models.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/579f4dc3e8163fc1185c94b4ed382050cb2517fc/memorycard/models.py#L6C1-L29C27)
  <br>
- 단순한 CRUD 기능만 빠르게 구현하기 위해서 views.py에서는 ViewSet을 사용하여 Subject와 Memorycard의 CRUD를 구현하였습니다.
    ```python
    class SubjectViewSet(ModelViewSet):
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer
        permission_classes = [IsAuthenticated]
        ...생략...
    
    class MemoryCardViewSet(ModelViewSet):
        queryset = MemoryCard.objects.all()
        serializer_class = MemoryCardSerailizer
        permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        ...생략...
    ```
    #### [⬆️ memorycard/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/579f4dc3e8163fc1185c94b4ed382050cb2517fc/memorycard/views.py#L37C1-L126C30)
<br>

## 7. 추가 기능
### 7.1. APP : chat

#### 7.1.1. 스터디 그룹 내에서 멤버들끼리 실시간 채팅이 가능하며, 기존 채팅 내역 조회가 가능합니다.
- Django Channels 라이브러리를 사용하여 실시간 채팅을 구현하였습니다.
- consumers.py에 Django Channels 라이브러리의 AsyncWebsocketConsumer를 상속받아 ChatConsumer 클래스를 작성하였으며, 이는 웹소켓 연결, 메시지 수신 및 발신을 비동기적으로 처리합니다.
- 웹소켓 연결을 담당하는 코드입니다. ⤵️
    ```python
    # chat/consumers.py
    class ChatConsumer(AsyncWebsocketConsumer):
        async def connect(self):
            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
            self.room_group_name = f"chat_{self.room_name}"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            chat_history = await self.get_chat_history()
            for chat in chat_history:
                await self.send(text_data=json.dumps({
                    "message": chat.content, 
                    "nickname": await database_sync_to_async(lambda: chat.user.nickname)(),
                    "profile_image": await database_sync_to_async(lambda: chat.user.profile_image.url)(),    
                }))
                
        async def disconnect(self, close_code):
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        ...생략...
    ```
- 채팅 수신 및 발신을 담당하는 코드입니다. ⤵️
    ```python
    # chat/consumers.py
    class ChatConsumer(AsyncWebsocketConsumer)
        ...생략...
        async def receive(self, text_data):
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]
            room_id = text_data_json["room_id"]
            user_id = text_data_json['user_id']
            nickname = await database_sync_to_async(lambda: User.objects.get(id=user_id).nickname)()
            profile_image = await database_sync_to_async(lambda: User.objects.get(id=user_id).profile_image.url)()
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat.message", "message": message, "room_id": room_id, "nickname": nickname, "profile_image": profile_image, "user_id": user_id}
            )
            await self.save_message(room_id, message, user_id)
    
        async def chat_message(self, event):
            message = event["message"]
            await self.send(text_data=json.dumps({
                "message": message,
                "nickname": event["nickname"],
                "profile_image": event["profile_image"],
            }))
        ...생략...
    ```
- 채팅 내역을 저장하는 것을 담당하는 코드입니다. ⤵️
    ```python
    # chat/consumers.py
    class ChatConsumer(AsyncWebsocketConsumer)
        ...생략...
        @database_sync_to_async
        def save_message(self, room_id, message, user_id):
            Chat.objects.create(chat_room=ChatRoom.objects.get(study_group__id=room_id), content=message, user=User.objects.get(id=user_id))
    
        @database_sync_to_async
        def get_chat_history(self):
            chat_history = Chat.objects.filter(chat_room__id=self.room_name)
            return list(chat_history)
        ...생략...
    ```
    #### [⬆️ chat/consumers.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/579f4dc3e8163fc1185c94b4ed382050cb2517fc/chat/consumers.py#L10)
    <br>
    
### 7.2. APP : memorycard

#### 7.2.1. 암기용 플래시 카드에 난이도와 북마크 기능을 추가하여 이를 통해 어려운 것만 별도로 학습할 수 있습니다.
- models.py의 MemoryCard 모델에 bookmark를 추가하였습니다.
    ```python
    class MemoryCard(models.Model):
        ...생략...
        bookmark = models.BooleanField(default=False)
        ...생략...
    ```
    #### [⬆️ memorycard/models.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/579f4dc3e8163fc1185c94b4ed382050cb2517fc/memorycard/models.py#L14C1-L29C27)
    <br>
- views.py의 get_queryset 설정을 통해 주제와 북마크 기능에 따라 필터링 할 수 있도록 하였습니다.
    ```python
    class MemoryCardViewSet(ModelViewSet):
        ...생략...
        def get_queryset(self):
            subject = self.request.GET.get('subject', '')
            bookmark = self.request.GET.get('bookmark', 'off')
            
            if subject and bookmark == 'on':
                return self.queryset.filter(subject__user=self.request.user, subject__id=subject, bookmark=True)
            elif subject and bookmark == "off":
                return self.queryset.filter(subject__user=self.request.user, subject__id=subject)
            return self.queryset.filter(subject__user=self.request.user)
    ```
    #### [⬆️ memorycard/views.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/579f4dc3e8163fc1185c94b4ed382050cb2517fc/memorycard/views.py#L96C1-L126C30)
    <br>

<br>

## 8. 개발하며 경험한 오류와 해결방법
### 8.1. simplejwt과 dj-rest-auth 설정 후 로그인 하였을 때 access_token만 받고, refresh_token을 못 받는 상황 발생
#### 해결방법
- settings.py의 'JWT_AUTH_HTTPONLY': 설정을 False로 설정하여 해결하였습니다.
```
Note [공식문서] 
JWT_AUTH_HTTPONLY를 True로 설정하면 refresh_token이 필요한 경우 refresh_token이 전송되지 않습니다. False로 설정하면 전송됩니다.
```
#### [⬆️ dj-rest-auth 공식문서](https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#configuration)
<br>

#### 왜?
- **True로 설정할 경우**
    - JWT을 HTTPOnly 쿠키로 보내게 되는데 이는 보안상의 이유로 클라이언트 스크립트가 쿠키에 직접 접근하는 것이 불가능합니다.
    - 이는 주로 refresh_token이 필요한 상황에서 문제가 생길 수 있는데, 그 이유는 refresh_token은 보통 클라이언트에서 JWT를 갱신하기 위해 사용되지만, HTTPOnly 쿠키로 JWT를 보내게 되면 클라이언트에서 refresh_token에 접근할 수 없기 때문입니다.
- **False로 설정할 경우**
    - dj-rest-auth는 JWT를 HTTPOnly가 아닌 쿠키로 보내게 되며 이는 클라이언트 스크립트가 쿠키에 직접 접근하는 것이 가능하므로, refresh_token을 사용하여 JWT를 갱신하는 것이 가능합니다.

<br>

### 8.2. dj-rest-auth에서 참조하는 username을 없애려고 할 때 username이 없다고 하는 에러메세지 발생
#### 해결방법
- AbstractUser 모델을 사용하지 말고 AbstractBaseUser 모델을 사용하고 필요한 필드들을 직접 정의
- settings.py에서 ACCOUNT_USER_MODEL_USERNAME_FIELD 설정을 none으로 설정
    ```python
    # settings.py
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None # 사용자 이름 필드 지정
    ```
#### 왜?
- AbstractUser를 상속받아 유저를 커스텀 하였기 때문에 username 필드를 완전히 제거하지 못하여 발생한 오류
- default값으로 username을 사용하지만, 모델에서는 사용하지않아 생기는 오류

<br>

### 8.3. model에서 blank=True를 적용하였으나, 클라이언트에서 요청 시 nikcname 필드가 blank일 수 없다는 메세지 발생
#### 해결방법
- serializers에서도 allow_blank=True를 설정
    ```python
    nickname = serializers.CharField(required=False, allow_blank=True)
    ```
    #### [⬆️ accounts/serializers.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/90b488c684bcf1761d00a6a086f57afc9ff45a90/accounts/serializers.py#L12C5-L12C71)

#### 왜?
- 모델의 blank=True는 해당 필드가 데이터베이스에 저장될 때 빈 값이 허용됨을 의미(데이터베이스 레벨에서의 유효성 검사) 
- 시리얼라이저에서 allow_blank=True를 설정해야만 클라이언트로부터 빈 문자열을 받았을 때 시리얼라이저의 유효성 검사를 통과할 수 있습니다.(입력 데이터의 유효성 검사)
- allow_blank=True를 설정하지 않을 경우 빈 값을 유효하지 않은 것으로 간주하고 오류 메시지를 반환

<br>

### 8.4. Router로 생성한 URL로 API 요청 시 404 Error 발생
#### 해결방법
- 코드 순서를 바꾼다.
    ```python
    memorycard/urls.py
    # 에러 발생 코드
    router = DefaultRouter()
    router.register(r'', MemoryCardViewSet, basename="memorycard")
    router.register(r'subject', SubjectViewSet, basename="memorycard")
    
    # 해결 코드
    router = DefaultRouter()
    router.register(r'subject', SubjectViewSet, basename="memorycard")
    router.register(r'', MemoryCardViewSet, basename="memorycard")
    ```
    #### [⬆️ memorycard/urls.py 소스 코드 링크](https://github.com/Quartett/StudyUs-BE/blob/90b488c684bcf1761d00a6a086f57afc9ff45a90/memorycard/urls.py#L5C1-L7C63)
- ViewSet에서 lookup_value_regex 속성을 통해 적용할 정규표현식을 바꾼다
    ```python
    memorycard/views.py
    class MemoryCardViewSet(ModelViewSet):
        queryset = MemoryCard.objects.all()
        serializer_class = MemoryCardSerailizer
        permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        lookup_value_regex = r'\d+'
    ```
#### 왜?
- rest_framework.routers의 Router들은 내부적으로 정해진 정규 표현식이 있습니다.
- ViewSet에서 /memorycard/ URL에 대한 url pattern의 pk 정규 표현식이 숫자 패턴이 아니라 문자열 패턴으로 등록이 되고 있었습니다.
- 즉, /memorycard/subject/의 요청은 memorycard 리소스에 대한 detail 요청으로 처리되어 pk=”subject”로 처리되었고 해당 pk를 찾을 수 없어 404 에러가 발생

<br>

### 8.5. DB에 데이터 입력 시, Unique 위반에 대한 오류
#### 해결방법
- serializer 클래스 내부에서 validate 메서드를 사용하여 검증을 진행하고 오류메시지 지정하기
    ```python
    from rest_framework import serializers

    class SubjectSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Subject
            fields = ('id', 'user', 'title')
            read_only_fields = ('user',)
    
        def validate_title(self, value):
            if Subject.objects.filter(user=self.context['request'].user, title=value).exists():
                raise serializers.ValidationError("이미 존재하는 주제입니다.")
            return value
    ```
- views.py의 ViewSet에서 create 메서드를 오버라이딩, try/except문으로 에러를 핸들링하여 오류메시지를 지정하기
    ```python
    class SubjectViewSet(ModelViewSet):
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer
        permission_classes = [IsAuthenticated]
    
        def get_queryset(self):
            return self.queryset.filter(user=self.request.user)
        
        def perform_create(self, serializer):
            serializer.save(user=self.request.user)
    
        def create(self, request, *args, **kwargs):
            try:
                return super().create(request, *args, **kwargs)
            except IntegrityError:
                error_message = {
                    "detail": "이미 존재하는 주제입니다."
                }
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
    ```
    기획한 응답값 형식은 키-밸류에 대한 모든 값을 지정하는 것이었기 때문에, 두번째 방법이 더 낫다고 판단하여 채택하였습니다.

<br>

## 9. 프로젝트 소감(어려웠던 점 & 배운 점)
