from django.shortcuts import render
from .serializer import LoginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User


def index(request):
    return render(request, 'index.html')


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            password = serializer.validated_data.get('password')
            print(phone_number)
            user = User.objects.filter(phone_number=phone_number).first()
            if user is not None and user.check_password(password):
                return Response(
                    data={
                        'id': user.id,
                        'username': user.username,
                        'user_roles': user.status,
                        'access_token': user.token()['access_token'],
                        'refresh_token': user.token()['refresh_token'],
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    data={
                        'success': False,
                        'message': 'Username or password is invalid.'
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
