from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.RepairWorksListViewSet.as_view()),
    path('<int:pk>/', views.RepairWorkViewSet.as_view())
]