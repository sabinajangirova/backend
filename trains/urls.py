from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.TrainsListViewSet.as_view()),
    path('<int:pk>/', views.TrainViewSet.as_view())
]