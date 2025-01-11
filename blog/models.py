from django.db import models
from django.utils.text import slugify

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
         
    def __str__(self):
        return self.name
    
    

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Blog Başlığı')
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
         
    def __str__(self):
        return self.title
    
    
class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Image for {self.blog.title}"