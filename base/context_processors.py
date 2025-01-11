from .models import *
from room.models import *
from service.models import *
from blog.models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect

def site_settings(request):
    
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uğurla abunə olundu!!!")
            return redirect('base:index')
    else:
        form = SubscribeForm()
    
    navigation_item = NavigationItem.objects.first()
    room_categories = RoomCategory.objects.all()
    rooms = Room.objects.all()
    brands = Brand.objects.all()
    services = Service.objects.all()
    about = About.objects.first()
    mission = Mission.objects.first()
    faqs = FAQ.objects.all()
    last_4_blogs = Blog.objects.all().order_by('-created_at')[:4]
    
    context = {
        'navigation_item': navigation_item,
        'categories' : room_categories,
        'rooms' : rooms,
        'brands' : brands,
        'services' : services,
        'about' : about,
        'mission' : mission,
        'faqs' : faqs,
        'form' : form,
        'last_blogs' : last_4_blogs
    }
    
    return context