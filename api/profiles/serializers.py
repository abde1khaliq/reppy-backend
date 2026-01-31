from rest_framework import serializers
from .models import UserProfile


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'bio',
                  'birthday', 'gender']

    def create(self, validated_data):
        user = self.context.get('user_instance')
        validated_data['user'] = user
        return super().create(validated_data)
