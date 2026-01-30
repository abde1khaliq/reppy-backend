from django.urls import path, include
from django.contrib import admin
from django.conf import settings
import debug_toolbar
from rest_framework import routers
from workout.views import WorkoutViewSet
from profiles.views import ProfilesViewSet
from .access_jwt import CustomTokenObtainPairView
from .refresh_jwt import CookieTokenRefreshView

router = routers.DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'profiles', ProfilesViewSet, basename='profiles')

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls')),
    path(r'reppy_api/v1/', include(router.urls)),
    path(r'auth/jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path(r'auth/jwt/refresh/', CookieTokenRefreshView.as_view(), name='jwt-refresh'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
