from django.shortcuts import render
from rest_framework import views, response, exceptions, permissions, generics
from . import authentication
# from . import services

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .serializer import UserSerializer
from rest_framework import filters
from .models import User
# class RegisterApi(views.APIView):
#     def post(self, request):
#         serializer = user_serializer.UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.validated_data
#         serializer.instance = services.create_user(user_dc=data)

#         return response.Response(data=serializer.data)

# class LoginApi(views.APIView):
#     def post(self, request):
#         email = request.data["email"]
#         password = request.data["password"]

#         user = services.user_email_selector(email=email)

#         if user is None:
#             raise exceptions.AuthenticationFailed("Invalid Credentials")

#         if not user.check_password(raw_password=password):
#             raise exceptions.AuthenticationFailed("Invalid Credentials")

#         token = services.create_token(user_id=user.id)

#         resp = response.Response()

#         resp.set_cookie(key="jwt", value=token, httponly=True)

#         return resp

class UserApi(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)
    
    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return User.objects.all()

    # def get_object(self):
    #     lookup_field_value = self.kwargs[self.lookup_field]

    #     obj = User.objects.get(pk=lookup_field_value)
    #     self.check_object_permissions(self.request, obj)

    #     return obj


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Successfully logged out"}

        return resp

# class LoginViewSet(ModelViewSet, TokenObtainPairView):
#     serializer_class = LoginSerializer
#     permission_classes = (AllowAny,)
#     http_method_names = ['post']

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             user = User.objects.get(email=request.data["email"], password=request.data["password"])
#             print(user)
#             # serializer.is_valid(raise_exception=True)
#         except TokenError as e:
#             print(serializer.error)
#             # raise InvalidToken(e.args[0])

#         return Response("ok", status=status.HTTP_200_OK)


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