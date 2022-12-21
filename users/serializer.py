from rest_framework import serializers
from . import services
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from .models import User
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    full_name = serializers.SerializerMethodField()
    phone_number = serializers.CharField()

    def get_full_name(self, obj):
        first_name = obj.first_name if obj.first_name is not None else ""
        last_name = obj.last_name if obj.last_name is not None else ""

        return first_name + " " + last_name

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=255)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff', 'created', 'updated']

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user

        
# from django.contrib.auth.models import Group, Permission

# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         fields = "__all__"


# class GroupSerializer(serializers.ModelSerializer):
#     permissions = PermissionSerializer(many=True)

#     class Meta:
#         model = Group
#         fields = ("id", "name", "permissions")

# class UserSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()
#     # user_permissions = PermissionSerializer(many=True)
#     # groups = GroupSerializer(many=True, read_only=True)

#     def get_full_name(self, obj):
#         first_name = obj.first_name if obj.first_name is not None else ""
#         last_name = obj.last_name if obj.last_name is not None else ""

#         return first_name + " " + last_name

#     class Meta:
#         model = User
#         fields = (
#             "email",
#             "phone_number",
#             "last_name",
#             "first_name",
#             "full_name",
#             "user_permissions",
#             "groups",
#             "id",
#         )