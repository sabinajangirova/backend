from django.urls import path
import users.views

urlpatterns=[
    path('register', users.views.RegistrationView.as_view(), name="register"),
    path('me', users.views.UserApi.as_view(), name="me"),
    path('list', users.views.UserListApi.as_view(), name="list")
    # path('api/login/', users.views.LoginViewSet.as_view(), name='login'),
    # path('api/refresh/', users.views.RefreshViewSet.as_view(), name='refresh'),
    # path('api/profile/', users.views.UserApi.as_view(), name='profile'),
    # path('api/logout/', users.views.LogoutApi.as_view(), name='logout')
]