from django.urls import path
from .views import index_view, room_view

urlpatterns = [
    path('',index_view, name='show all rooms' ),
    path("<str:room_name>/", room_view, name="chat"),

]