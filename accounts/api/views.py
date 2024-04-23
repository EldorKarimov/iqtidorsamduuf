from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not CustomUser.objects.filter(username = username).exists():
            raise AuthenticationFailed(_("User not found"))
        
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "user":{
                    "id":user.id,
                    "username": user.username,
                    "full_name": user.get_full_name()
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            },
            status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error":"Invalid credentials", 
                },
                status=status.HTTP_401_UNAUTHORIZED
            )