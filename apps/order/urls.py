from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("buy", views.buy, name='buy'),
    path("getStatus", views.get_status, name="getStatus"),
    path("updateStatus", views.update_status, name="updateStatus")
]