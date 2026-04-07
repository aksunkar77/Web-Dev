"""
Django settings for shop_back project.
"""

from pathlib import Path

# Үндсэн зам
BASE_DIR = Path(__file__).resolve().parent.parent

# Аюулгүй байдлын тохиргоо
SECRET_KEY = 'django-insecure-86!vixwpkc&3-**1l5wj9loyeu@5%92(lckr#e72g9@pe*!5zz'
DEBUG = True
ALLOWED_HOSTS = []

# Суулгасан апп-ууд (Энд хаалт дутуу байсныг засав)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',       # CORS тохиргоо
    'rest_framework',    # Django REST Framework
    'api',               # Чиний үүсгэсэн api апп
]

# Middleware тохиргоо
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop_back.wsgi.application'

# Өгөгдлийн сан (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Нууц үг шалгагч
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Хэл болон цагийн бүс
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статик файлууд
STATIC_URL = 'static/'

# CORS-ыг бүх хаягт зөвшөөрөх
CORS_ALLOW_ALL_ORIGINS = True