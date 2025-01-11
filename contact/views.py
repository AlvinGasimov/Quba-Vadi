from django.shortcuts import render, redirect
from .forms import ContactForm
from room.models import Room

def contact(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'rooms': rooms
    })