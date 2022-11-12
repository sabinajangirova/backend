from rest_framework import serializers
from . import services


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