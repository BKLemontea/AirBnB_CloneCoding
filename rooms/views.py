from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView
from django.shortcuts import render, redirect, reverse
from django_countries import countries
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users import mixins as user_mixins
from . import models, forms

class HomeView(ListView):
    
    """ HomeView Definition """
    
    model = models.Room
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    # page_kwarg = "page"
    context_object_name = "rooms"

# class 기반 view
class RoomDetail(DetailView): #위와 다르게 404에러가 나면 장고가 알아서 Not Found 페이지로 보내준다.
    
    """ RommDetail Definition """
    
    model = models.Room

class SearchView(View):
    
    def get(self, request):
        country = request.GET.get("country")

        if country:
            
            form = forms.SearchForm(request.GET)
            
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")
                
                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                
                paginator = Paginator(qs, 10, orphans=5)
                
                page = request.GET.get("page", 1)
                
                rooms = paginator.get_page(page)
                
                return render(request, "rooms/search.html", {
                    "form":form,
                    "rooms":rooms,
                })
                
        else:
            form = forms.SearchForm()
        
        return render(request, "rooms/search.html", {"form":form})
    
class EditRoomView(user_mixins.LoggedInOnlyView, UpdateView):
    
    model = models.Room
    template_name = "rooms/room_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )
    
    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room
    
class RoomPhotosView(user_mixins.LoggedInOnlyView, DetailView):
    
    model = models.Room
    template_name = "rooms/room_phtos.html"
    
    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room

@login_required  
def delete_photo(request, room_pk, photo_pk):
    user = request.user
    try:
        room = models.Room.objects.get(pk=room_pk)
        if room.host.pk != user.pk:
            messages.error(request, "Can't delete that photo")
        else:
            """
            photo = models.Photo
            photo.delete()
            아래 방법과는 다르게 특정 사진만 삭제 할 수 있다.
            """
            # 필터에 속한 모든 사진을 삭제한다. 이 경우에는 pk에 해당하는 사진이 하나 뿐이니 위와 동일하게 작동된다.
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("rooms:photos", kwargs={'pk':room_pk}))
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
    