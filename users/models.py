from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import PermissionsMixin, Group
from trainstations.models import TrainStation

class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name:str, last_name:str, email:str,phone_number:str, password:str = None, role:str = None, station:int = None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.role=role
        user.station=station
        user.save()
        return user

    def create_superuser(self, first_name:str, last_name:str, email:str, phone_number:str, password:str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user


class User(auth_models.AbstractUser, PermissionsMixin):
    class UserRole(models.TextChoices):
        STATION_WORKER = 'Station worker'
        TRAIN_CONDUCTOR = 'Train conductor'

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True, default="")
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    station = models.ForeignKey(TrainStation, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=25, choices=UserRole.choices, null=False, blank=False, default=UserRole.TRAIN_CONDUCTOR)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

# class StationWorker(User):
#     class Meta:
#         permissions = [('repairworks.view_repairWork'), ('repairworks.add_repairWork'), ('repairworks.change_repairWork'), ('repairworks.delete_repairWork')]

# class TrainConductor(User):
#     class Meta:
#         permissions = [('repairworks.view_repairWork')]