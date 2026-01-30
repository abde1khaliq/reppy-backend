from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get("refresh")

        if refresh:
            response.set_cookie(
                key='refresh_token',
                value=refresh,
                httponly=True,
                secure=False,
                samesite='Lax',
                path='/',
            )
            del response.data["refresh"]

        return response