"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from categories.api.viewsets import CategoryViewSet
from orders.api.viewsets import OrderViewSet
from payments.api.viewsets import PaymentViewSet
from products.api.viewsets import ProductViewSet
from tables.api.viewsets import TableViewSet
from users.api import urls as user_auth_urls
from users.api.viewsets import UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="API docs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("categories", CategoryViewSet, basename="categories")
router.register("products", ProductViewSet, basename="products")
router.register("tables", TableViewSet, basename="tables")
router.register("orders", OrderViewSet, basename="orders")
router.register("payments", PaymentViewSet, basename="payments")

urlpatterns = [
    path(
        "docs/",
        schema_view.with_ui(
            "swagger",
        ),
        name="schema-swagger-ui",
    ),  # api documentation
    path("admin/", admin.site.urls),
    path("api/", include(user_auth_urls)),  # auth/me  auth/login/
    path("api/", include(router.urls)),
]
