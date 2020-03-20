from django.urls import path
from . import views

appname = "rooms"

urlpatterns = [path("1", views.room_detail, name = "detail")
