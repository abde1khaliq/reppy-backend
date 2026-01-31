from django.urls import path, include
from django.contrib import admin
from django.conf import settings
import debug_toolbar
from .access_jwt import CustomTokenObtainPairView
from .refresh_jwt import CookieTokenRefreshView

API_PREFIX = 'reppy_api'

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path(r'auth/jwt/refresh/', CookieTokenRefreshView.as_view(), name='jwt-refresh'),
    # Apps Url endpoints
    path(f'{API_PREFIX}/', include("workout.urls")),
    path(f'{API_PREFIX}/', include("profiles.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
