from django.shortcuts import render, redirect
from .models import HomeHotel
from .forms import SubscribeForm
from django.contrib import messages
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def index(request):
    home_hotels = HomeHotel.objects.all()
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uğurla abunə olundu!!!")
            return redirect('base:index')
    else:
        form = SubscribeForm()
        
    context = {
        'home_hotels': home_hotels,
        'form' : form
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')



def set_language(request, language):
    if language not in dict(settings.LANGUAGES):
        return HttpResponseRedirect("/")

    referer = request.META.get("HTTP_REFERER", "/")
    try:
        view = resolve(urlparse(referer).path)
        translation.activate(language)
        app_name = view.app_name if hasattr(view, 'app_name') else None
        view_name = f"{app_name}:{view.url_name}" if app_name else view.url_name

        response = HttpResponseRedirect(
            reverse(view_name, args=view.args, kwargs=view.kwargs)
        )
    except Resolver404:
        response = HttpResponseRedirect("/")
    
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response