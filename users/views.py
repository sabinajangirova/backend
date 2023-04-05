from django.shortcuts import render
from rest_framework import views, response, exceptions, permissions, generics
from . import authentication
# from . import services

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .serializer import UserSerializer
from rest_framework import filters
from .models import User

class UserApi(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)

class UserListApi(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        role = self.request.query_params.get('role')
        if role is not None:
            queryset = queryset.filter(role=role)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Successfully logged out"}

        return resp
    
class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)
        return Response(user.data, status=status.HTTP_201_CREATED)


class RefreshViewSet(ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)