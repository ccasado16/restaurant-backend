from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        password = request.data["password"]

        if password:
            request.data["password"] = make_password(password)
        else:
            request.data["password"] = request.user.password

        return super().update(request, *args, **kwargs)
