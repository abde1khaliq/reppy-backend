from django.db import models


class Workout(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Exercise(models.Model):
    category = models.ForeignKey(
        Category, related_name="exercises", on_delete=models.PROTECT
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name