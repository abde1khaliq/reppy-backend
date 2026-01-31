from rest_framework import serializers
from .models import Workout, WorkoutHistory


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "user", "title", "created_at"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        user = self.context.get('user_instance')
        validated_data['user'] = user
        return super().create(validated_data)


class WorkoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutHistory
        fields = ["id", "workout", "performed_at"]
