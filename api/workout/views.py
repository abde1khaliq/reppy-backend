from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workout, WorkoutHistory, WorkoutExercise
from .serializers import WorkoutSerializer, WorkoutHistorySerializer, WorkoutExerciseSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'user_instance': self.request.user}


class WorkoutHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WorkoutHistory.objects.all()
    serializer_class = WorkoutHistorySerializer


class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutExerciseSerializer

    def get_queryset(self):
        return WorkoutExercise.objects.filter(workout=self.kwargs['workout_pk'])

    def get_serializer_context(self):
        return {'workout_instance': self.kwargs['workout_pk']}
