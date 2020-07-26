from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blog_all = Blog.objects.all()
    paginator = Paginator(blog_all, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    
    return render(request, "home.html", {'blogs': blogs})


def detail(request, blog_id):
    if request.user.is_authenticated():
        blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {"blog": blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.content = request.GET['content']
    blog.created_at = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))