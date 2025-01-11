from django.db import models
from django.utils.text import slugify

class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Room Categories'


class Room(models.Model):
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    mature_capacity = models.IntegerField()
    young_capacity = models.IntegerField()
    bed_position = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    owner_number = models.CharField(max_length=50, null=True, blank=True)
    enter_time = models.TimeField()
    exit_time = models.TimeField()
    star_number = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.number}"
    
    class Meta:
        verbose_name_plural = 'Rooms'
    
    
class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for {self.room.name}"
    

class RoomSupply(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='supplies')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} for {self.room.name}"
    
    
class RoomFeature(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} for {self.room.name}"