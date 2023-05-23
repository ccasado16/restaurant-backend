from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.viewsets import UserViewSet
from users.views import UserView

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/me/", UserView.as_view()),
]
