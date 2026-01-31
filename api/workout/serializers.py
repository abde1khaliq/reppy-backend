from rest_framework import serializers
from .models import Workout, WorkoutHistory, WorkoutExercise


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


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ["id", "sets", "reps", "exercise"]

    def create(self, validated_data):
        workout = self.context.get('workout_instance')
        validated_data['workout_id'] = workout
        return super().create(validated_data)
