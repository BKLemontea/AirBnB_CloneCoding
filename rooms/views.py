from django.views.generic import ListView, DetailView
# from django.http import Http404
from django.shortcuts import render
from django_countries import countries
from . import models

class HomeView(ListView):
    
    """ HomeView Definition """
    
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    # page_kwarg = "page"
    context_object_name = "rooms"
    
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    """
    

# function 기반 view
"""
def room_detail(request,pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room":room})
    except models.Room.DoesNotExist:
        raise Http404()
"""

# class 기반 view
class RoomDetail(DetailView): #위와 다르게 404에러가 나면 장고가 알아서 Not Found 페이지로 보내준다.
    
    """ RommDetail Definition """
    
    model = models.Room

def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("counrty", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    
    form = {
        "city":city,
        "s_country":country,
        "s_room_type":room_type,
        "price":price,
        "guests":guests,
        "bedrooms":bedrooms,
        "beds":beds,
        "baths":baths,
        "s_amenities":s_amenities,
        "s_facilities":s_facilities,
        "instant":instant,
        "super_host":super_host,
    }
    
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facilitiy.objects.all()
    
    choices = {
        "countries":countries,
        "room_types":room_types,
        "amenities":amenities,
        "facilities":facilities,
    }
    
    return render(request, "rooms/search.html", {
        **form,
        **choices,
    })
        