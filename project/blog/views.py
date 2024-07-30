from django.shortcuts import render, get_object_or_404

from .models import *

def blog_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    context = {
        'blog':blog
    }
    return render(request, "blog/blog.html", context)