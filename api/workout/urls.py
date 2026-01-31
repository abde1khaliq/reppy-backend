from rest_framework_nested import routers
from .views import WorkoutViewSet, WorkoutHistoryViewSet

app_name = 'workouts'

router = routers.DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')

workout_router = routers.NestedDefaultRouter(router, r'workouts', lookup='workout')
workout_router.register(r'history', WorkoutHistoryViewSet, basename='workout-history')

urlpatterns = router.urls + workout_router.urls
