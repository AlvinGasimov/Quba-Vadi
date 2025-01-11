from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='services_icon/')
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='services_images/')

    def __str__(self):
        return self.service.title


class ServiceVideo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.service.title