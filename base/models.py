from django.db import models

class NavigationItem(models.Model):
    title = models.CharField(max_length=100)
    navbar_img = models.ImageField(upload_to='navbar_img/')
    footer_img = models.ImageField(upload_to='footer_img/')
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=200, blank=True, null=True)
    tiktok_link = models.URLField(max_length=200, blank=True, null=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    map_link = models.URLField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeHotel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home_hotel_img/')
    resp_image = models.ImageField(upload_to='home_hotel_resp_img/')
    star_number = models.IntegerField()
    owner_phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.title
      
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_img/')

    def __str__(self):
        return self.name    

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='about_img/')
    customer_count = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'About'      
        
class Mission(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='mission_img/')
    video_url = models.CharField(max_length=400)

    def __str__(self):
        return self.title  
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class Subscribe(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email Ünvanı")

    def __str__(self):
        return self.email