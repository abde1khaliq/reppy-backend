from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workout, WorkoutHistory
from .serializers import WorkoutSerializer, WorkoutHistorySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_serializer_context(self):
        return {'user_instance': self.request.user}


class WorkoutHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WorkoutHistory.objects.all()
    serializer_class = WorkoutHistorySerializer
