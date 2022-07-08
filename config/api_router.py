from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
urlpatterns = [
    path("users/", include("mqtt_rest.users.urls")),
    path("mqtts/", include("mqtt_rest.mqtts.urls")),
]
urlpatterns += router.urls
