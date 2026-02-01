from rest_framework import serializers
from .models import UserProfile


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'bio',
                  'birthday', 'gender']

    def create(self, validated_data):
        user = self.context.get('user_instance')
        validated_data['user'] = user
        return super().create(validated_data)


class ListProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'bio', 'birthday',
                  'gender', 'status_message', 'current_streak']
