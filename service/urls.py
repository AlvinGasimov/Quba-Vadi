from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [
    path('<slug:service_slug>', service_details, name='service_details'),
]