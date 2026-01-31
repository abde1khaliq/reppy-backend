from rest_framework_nested import routers
from .views import WorkoutViewSet, WorkoutHistoryViewSet, WorkoutExerciseViewSet, ExerciseViewSet

app_name = 'workouts'

router = routers.DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'exercises', ExerciseViewSet, basename='exercises')

workout_exercises = routers.NestedDefaultRouter(
    router, r'workouts', lookup='workout')
workout_exercises.register(
    r'exercises', WorkoutExerciseViewSet, basename='workout-exercise')

workout_router = routers.NestedDefaultRouter(
    router, r'workouts', lookup='workout')
workout_router.register(r'history', WorkoutHistoryViewSet,
                        basename='workout-history')

urlpatterns = router.urls + workout_exercises.urls + workout_router.urls
