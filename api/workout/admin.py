from django.contrib import admin
from .models import Exercise, Workout, Category, WorkoutExercise

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Category)
admin.site.register(WorkoutExercise)
