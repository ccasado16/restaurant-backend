from rest_framework.routers import DefaultRouter

from categories.api.viewsets import CategoryViewSet


router = DefaultRouter()

router.register("categories", CategoryViewSet, basename="categories")