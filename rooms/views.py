from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5) #orphans은 마지막 페이지의 항목 수가 5개 이하일 경우 그전 페이지에서 보여줌.
    try:
        # paginator.get_page()는 에러가 발생하면 마지막 페이지를 보여줌
        # paginator.page()는 에러가 발생하면 에러 페이지를 보여줌
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={
        "page":rooms
        })
    except EmptyPage:
        return redirect("/")
    