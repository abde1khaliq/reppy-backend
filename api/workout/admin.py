from django.contrib import admin
from .models import Exercise, Workout, Category

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Category)
