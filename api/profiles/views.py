from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import ProfilesSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request_user': self.request.user}

    @action(detail=False, methods=['GET'])
    def me(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response(
                {"detail": "No profile found for this user."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(profile)
        return Response(serializer.data)
