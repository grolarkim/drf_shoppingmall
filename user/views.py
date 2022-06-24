from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from user.views import User
from user.serializers import UserLoginSerializer, UserSerializer
from user.permissions import PostOrLoginRequired


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인에 성공하셨습니다."}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        logout(request)
        return Response({"message": "로그아웃 하셨습니다."}, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    permission_classes = [PostOrLoginRequired]
    
    def get(self, request):
        return

    def post(self, request):
        return
    
    def put(self, request):
        return
    
    def delete(self, request):
        return
    

