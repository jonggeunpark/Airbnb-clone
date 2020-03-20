from django.urls import path
from rooms import views as room_views

appname = "core"
urlpatterns = [path("", room_views.HomeView.as_view())]
