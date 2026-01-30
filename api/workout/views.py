from rest_framework import viewsets
from rest_framework import generics
from .models import Workout, WorkoutHistory
from .serializers import WorkoutSerializer, WorkoutHistorySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutListView(generics.ListAPIView):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class WorkoutHistoryView(generics.ListAPIView):
    serializer_class = WorkoutHistorySerializer

    def get_queryset(self):
        workout_id = self.kwargs["pk"]
        return WorkoutHistory.objects.filter(workout_id=workout_id)
