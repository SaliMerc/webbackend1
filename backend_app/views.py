from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def blog(request):
    posts=BlogPost.objects.all()
    return render(request, 'blog.html', {'posts':posts})

def blog_details(request,id):
    post=get_object_or_404(BlogPost,id=id)
    return render(request, 'blog_details.html', {'post':post})