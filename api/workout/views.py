from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from .models import Workout, WorkoutHistory, WorkoutExercise, Exercise
from .serializers import WorkoutSerializer, WorkoutHistorySerializer, ListWorkoutExerciseSerializer, CreateWorkoutExerciseSerializer, ExerciseSerializer
from rest_framework.response import Response


class WorkoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'user_instance': self.request.user}


class WorkoutHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutHistorySerializer

    def get_queryset(self):
        return WorkoutHistory.objects.filter(user=self.request.user)


class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutExercise.objects.filter(workout=self.kwargs['workout_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateWorkoutExerciseSerializer
        return ListWorkoutExerciseSerializer

    def get_serializer_context(self):
        return {'workout_instance': self.kwargs['workout_pk']}

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return super().create(request, *args, **kwargs)


class ExerciseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
