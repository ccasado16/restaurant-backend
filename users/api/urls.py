from django.urls import include, path

from users.api.router import router


urlpatterns = [
    path("", include(router.urls)),
]
