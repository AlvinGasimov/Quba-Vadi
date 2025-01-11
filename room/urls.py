from django.urls import path
from .views import *

app_name = 'room'

urlpatterns = [
    path('', rooms, name='rooms'),
    path('<slug:room_slug>/', room_details, name='room-details')
]