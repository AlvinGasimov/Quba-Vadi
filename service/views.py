from django.shortcuts import render, get_object_or_404
from .models import *

def service_details(request, service_slug):
    
    service = get_object_or_404(Service, slug=service_slug)
    
    context = {
        'service': service
    }
    return render(request, 'services.html', context)