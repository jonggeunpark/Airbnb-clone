from django.shortcuts import render
from rooms import models as rooms_models


def all_rooms(request):
    all_rooms = rooms_models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
