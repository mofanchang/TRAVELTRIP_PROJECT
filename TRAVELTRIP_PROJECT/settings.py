import os
from pathlib import Path

# 專案根目錄
BASE_DIR = Path(__file__).resolve().parent.parent

# # 安全設定
SECRET_KEY = 'OVxH1411eRyGOifMp04Qd0PsNyUFqRBXCAhVtQC747ka21zyDX_N7QxNDcaJ6U5xEeY'
DEBUG = True
# ALLOWED_HOSTS = []

# 應用程式註冊
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自訂 apps
    'accounts',
    'trips',
    'cart',
    'bookings',
    'chatbot',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

# 自訂使用者模型
AUTH_USER_MODEL = 'accounts.CustomUser'

# 中介軟體
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # ← 加在這裡
]



# 模板設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'TRAVELTRIP_PROJECT','templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ...existing code...
ROOT_URLCONF = 'TRAVELTRIP_PROJECT.urls'

WSGI_APPLICATION = 'TRAVELTRIP_PROJECT.wsgi.application'
# ...existing code...

# SQLite 預設資料庫（可改 PostgreSQL）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'traveltrip_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': '172.23.180.176',
        'PORT': '5432',
    }
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'  # 靜態檔案網址前綴
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # collectstatic 後的輸出路徑（部署時用）
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'TRAVELTRIP_PROJECT', 'static'),
]

LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'