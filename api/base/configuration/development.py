from .config import *
from decouple import config, Csv
import dj_database_url
from datetime import timedelta


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    "default": dj_database_url.parse(
        config("SUPABASE_DB_URL")
    )
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


INTERNAL_IPS = [
    "127.0.0.1",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://reppy-topaz.vercel.app",
]


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=4),
}
