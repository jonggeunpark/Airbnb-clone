from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    """ HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request):
    render(request, "rooms/detail.html")


"""
from math import ceil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)

    try:
        rooms = paginator.page(page)
        return render(request, "rooms/home.html", {"page": rooms})
    except (EmptyPage, PageNotAnInteger):
        return redirect("/")
"""
