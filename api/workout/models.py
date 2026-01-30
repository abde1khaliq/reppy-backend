from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Workout(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workouts",)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    category = models.ForeignKey(
        Category, related_name="exercises", on_delete=models.PROTECT
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="workout_exercises")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.exercise.name} ({self.sets}x{self.reps})"


class WorkoutHistory(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="history")
    performed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.workout.title} at {self.performed_at}"
