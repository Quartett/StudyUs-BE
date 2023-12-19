from pathlib import Path
import environ
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# 환경설정 env
env = environ.Env(
    DEBUG=(bool, False),
)

######################
#  배포 버전 시 수정 필요 #
######################
# 개발용은 .env.dev
# 실서버용은 .env.prod
environ.Env.read_env(os.path.join(BASE_DIR, ".env.prod"))
######################
######################

SECRET_KEY = env('SECRET_KEY')

######################
#  배포 버전 시 수정 필요 #
######################
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ["*"]
######################
######################


# Application definition
INSTALLED_APPS = [
    "corsheaders",
    "daphne",
    # drf package
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "drf_spectacular",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # custom apps
    "chat",
    "study",
    "accounts",
]

MIDDLEWARE = [
    # cors 미들웨어
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
]

# CORS 관련
CORS_ALLOW_METHODS = [  # 허용할 옵션
    "*"
]
CORS_ALLOW_HEADERS = [ # 허용할 헤더
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "studyus.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "studyus.wsgi.application"
ASGI_APPLICATION = "studyus.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        }
    }
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": env('DATABASE_ENGINE'),
        "NAME": env('DATABASE_NAME'),
        "USER": env('DATABASE_USER'),
        "PASSWORD": env('DATABASE_PASSWORD'),
        "HOST": env('DATABASE_HOST'),
        "PORT": env('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "accounts.StudyUsUser"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# SPECTACULAR SETTINGS
SPECTACULAR_SETTINGS = {
    'TITLE': 'StudyUs API Document',
    'DESCRIPTION': '스터디어스 API 문서입니다.',
    'CONTACT': {'name': 'Quartett', 'url': 'https://github.com/Quartett/StudyUs-BE', 'email': 'huny3410@gmail.com'},
    # Swagger UI를 좀더 편리하게 사용하기위해 기본옵션들을 수정한 값들입니다.
    'SWAGGER_UI_SETTINGS': {
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/  <- 여기 들어가면 어떤 옵션들이 더 있는지 알수있습니다.
        'dom_id': '#swagger-ui',  # required(default)
        'layout': 'BaseLayout',  # required(default)
        'deepLinking': True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        'persistAuthorization': True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        'displayOperationId': True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        'filter': True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다
    },
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # OAS3 Meta정보 API를 비노출 처리합니다.
}

REST_AUTH = {
    'LOGIN_SERIALIZER': 'accounts.serializers.LoginSerializer',
    'REGISTER_SERIALIZER': 'accounts.serializers.RegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserDetailsSerializer',
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'my-access-token',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'JWT_AUTH_HTTPONLY':False,
    'JWT_AUTH_RETURN_EXPIRATION': True,
}

ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # 사용자 이름 필드 지정
OLD_PASSWORD_FIELD_ENABLED = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60), 
    # 편의상 access token 유효기간 개발 단계에서 60분으로 설정 추후 5분으로 수정 필요
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 이메일 인증 관련 설정
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
EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'account/confirmation_signup_message.txt'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[studyus]'