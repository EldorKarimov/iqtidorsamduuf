from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _
from accounts.hemisAPI import HemisApi


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        obj = HemisApi()
        data = obj.user_data_json(username=username, password=password)
        if data == 'error':
            raise exceptions.AuthenticationFailed(detail=_("login or password error"))
        data = data.get('data')
        if CustomUser.objects.filter(username = data.get('student_id_number')).exists():
            user = authenticate(request, username = username, password = password)
            if user is not None:
                refresh = RefreshToken.for_user(user=user)
                return Response({
                    "success":True,
                    "user":{
                        "id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "patronymic": user.patronymic,
                        "phone": user.phone,
                        "image": user.image_url,
                        "group": user.group,
                        "direction": user.direction,
                    },
                    "refresh": str(refresh),
                    "access_token": str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail":_("username or password error")},  status=status.HTTP_401_UNAUTHORIZED)

        else:
            user = CustomUser.objects.create(
                username = data.get('student_id_number'),
                first_name = data.get('first_name'),
                last_name = data.get('second_name'),
                patronymic = data.get('third_name'),
                phone = data.get('phone'),
                image_url = data.get('image'),
                direction = data.get('specialty').get('name'),
                group = data.get('group').get('name'),
            )
            user.password = make_password(password)
            user.save()
            refresh = RefreshToken.for_user(user=user)
            return Response({
                "success":True,
                "user":{
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "patronymic": user.patronymic,
                    "phone": user.phone,
                    "image": user.image_url,
                    "group": user.group,
                    "direction": user.direction,
                },
                "refresh": str(refresh),
                "access_token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)