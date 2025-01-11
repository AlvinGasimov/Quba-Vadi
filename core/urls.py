"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('base.urls', namespace='base')),
    path('rooms/', include('room.urls', namespace='room')),
    path('services/', include('service.urls', namespace='service')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('user/', include('user.urls', namespace='user')),
    path('rosetta/', include('rosetta.urls')),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)