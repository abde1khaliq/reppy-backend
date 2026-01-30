from django.urls import path
from .views import WorkoutListView, WorkoutHistoryView

urlpatterns = [
    path("reppy_api/v1/workouts", WorkoutListView.as_view(), name="workout-list"),
    path("reppy_api/v1/workouts/<int:pk>/history",
         WorkoutHistoryView.as_view(), name="workout-history"),
]
