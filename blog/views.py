from django.shortcuts import render, get_object_or_404
from .models import BlogCategory, Blog
from django.core.paginator import Paginator
from django.db.models import Q


def blogs(request):
    
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search', '')
    blogs = Blog.objects.all().order_by('-created_at')
    
    if category_slug:
        category = BlogCategory.objects.filter(slug=category_slug).first()
        blogs = blogs.filter(category=category) if category else Blog.objects.none()

    if search_query:
        blogs = blogs.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
    
    blog_categories = BlogCategory.objects.all()
    
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'selected_category': category_slug,
        'search_query': search_query,
        'blog_categories' : blog_categories
    }
    
    return render(request, 'blogs.html', context)


def blog_details(request, blog_slug):
    
    blog = get_object_or_404(Blog, slug=blog_slug)
    blog_categories = BlogCategory.objects.all()
    
    context = {
        'blog' : blog,
        'blog_categories' : blog_categories
    }
    return render(request, 'blog-details.html', context)