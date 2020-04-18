from django.shortcuts import redirect, reverse
from rooms import models as room_models
from . import models

# Create your views here.
def save_room(request, pk):
    room = room_models.Room.objects.get_or_none(pk=pk)
    if room is not None:
        the_list, _ = models.List.objects.get_or_create(user=request.user, name="My Favourites Houses")
        the_list.room.add(room)
    return redirect(reverse("rooms:detail", kwargs={"pk":pk}))