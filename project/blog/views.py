from django.shortcuts import render, get_object_or_404

from .models import *

def blog_view(request, id):
    # Handle post request here to save to reading list
    blog = get_object_or_404(Blog, id=id)
    context = {
        'blog':blog
    }
    return render(request, "blog/blog.html", context)

# Add a parser for markdown to tailwind