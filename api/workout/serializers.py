from rest_framework import serializers
from .models import Workout, WorkoutExercise, WorkoutHistory


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['title']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(
        source="exercise.name", read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ["exercise_name", "sets", "reps"]


class WorkoutSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "title", "created_at", "workout_exercises"]


class WorkoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutHistory
        fields = ["id", "performed_at"]
