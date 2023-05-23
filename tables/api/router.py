from rest_framework.routers import DefaultRouter

from tables.api.viewsets import TableViewSet


router = DefaultRouter()

router.register("tables", TableViewSet, basename="tables")
