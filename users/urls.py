from django.urls import path
import users.views

urlpatterns=[
    path('register', users.views.RegistrationView.as_view(), name="register"),
    path('me', users.views.UserApi.as_view(), name="me"),
]