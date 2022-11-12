from django.urls import path
import users.views

urlpatterns=[
    path('register/', users.views.RegisterApi.as_view(), name="register"),
    path('login/', users.views.LoginApi.as_view(), name='login'),
    path('profile/', users.views.UserApi.as_view(), name='profile'),
    path('logout/', users.views.LogoutApi.as_view(), name='logout')
]