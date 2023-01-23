from django.urls import path

from . import views

urlpatterns = [
    path('', views.RepairWorkCreateView.as_view(), name='create'),
]