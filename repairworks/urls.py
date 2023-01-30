from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.RepairWorkViewSet)

urlpatterns = [
    path('', include(router.urls))
]