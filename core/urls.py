from django.urls import path
from rooms import views as room_views

app_name = "core" # app_name의 이름은 config/urls.py의 namespace의 이름과 같아야 한다.

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]
