from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

GENDERS = [
    ('CYO', 'Choose your gender:'),
    ('male', 'Male'),
    ('female', 'Female'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.CharField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        choices=GENDERS,
        default='CYO',
        max_length=30
    )
    gender = models.CharField(
        choices=GENDERS, max_length=30, null=True, blank=True)
    status_message = models.CharField(max_length=100, null=True, blank=True)
    current_streak = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname or self.user.username
