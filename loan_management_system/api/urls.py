from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import retrieve_manufacturers_unique_id

app_name = "api"

router_v1 = DefaultRouter()


urlpatterns = [
    path(
        "contract/<int:pk>/",
        retrieve_manufacturers_unique_id,
        name="unique-manufacturers-id",
    ),
    path("", include(router_v1.urls)),
]
