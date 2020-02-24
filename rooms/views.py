from django.views.generic import ListView, DetailView
# from django.http import Http404
# from django.shortcuts import render
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
    
        