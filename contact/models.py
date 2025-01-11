from django.db import models
from room.models import Room

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad")
    phone = models.CharField(max_length=15, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email Ünvanı")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="contacts", verbose_name="Otaq")
    message = models.TextField(blank=True, null=True, verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Göndərilmə Tarixi")

    def __str__(self):
        return f"{self.name} ({self.email})"
