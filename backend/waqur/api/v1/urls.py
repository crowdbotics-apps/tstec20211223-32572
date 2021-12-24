from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Test123ViewSet

router = DefaultRouter()
router.register("test123", Test123ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
