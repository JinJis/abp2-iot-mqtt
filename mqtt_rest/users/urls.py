from django.urls import path

from mqtt_rest.users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="users-redirect"),
    path("~update/", view=user_update_view, name="users-update"),
    path("<str:username>/", view=user_detail_view, name="users-detail"),
]
