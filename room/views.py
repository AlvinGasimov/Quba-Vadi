from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

def rooms(request):
    
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search', '')
    rooms = Room.objects.all().order_by('-created_at')
    
    if category_slug:
        category = RoomCategory.objects.filter(slug=category_slug).first()
        rooms = rooms.filter(category=category) if category else Room.objects.none()

    if search_query:
        rooms = rooms.filter(
            Q(name__icontains=search_query) | Q(number__icontains=search_query) | Q(description__icontains=search_query)
        )
    
    paginator = Paginator(rooms, 16)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'rooms' : rooms,
        'category_slug' : category_slug
    }
    
    return render(request, 'rooms.html', context)


def room_details(request, room_slug):
    
    room = get_object_or_404(Room, slug=room_slug)
    context = {
        'room' : room
    }
    
    return render(request, 'room-details.html', context)