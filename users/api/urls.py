from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import UserView

# For user authentication
urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/me/", UserView.as_view()),
]
