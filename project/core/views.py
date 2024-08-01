from django.shortcuts import render
from blog.models import *

from django.shortcuts import render

def coming_soon(request):
    if request.user.is_authenticated:
        userprofile = Userprofile.objects.get(user=request.user)
        context = {
            'user': userprofile,
        }
        return render(request, 'core/coming_soon.html', context)
    else:
        return render(request, 'core/coming_soon.html')
    
def index(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()
    if request.user.is_authenticated:
        userprofile = Userprofile.objects.get(user=request.user)
        list = ReadingList.objects.filter(user=userprofile)
        context = {
            'blogs': blogs,
            'tags': tags,
            'user': userprofile,
            'list': list,
        }
    else:
        context = {
            'blogs': blogs,
            'tags': tags,
        }
    return render(request, 'core/index.html', context)

def tag(request, tag):
    request_tag = Tag.objects.get(tag=tag)
    blogs = Blog.objects.filter(tags=request_tag)
    
    if request.user.is_authenticated:
        userprofile = Userprofile.objects.get(user=request.user)
        list = ReadingList.objects.filter(user=userprofile)
        context = {
            'blogs': blogs,
            'tags': request_tag,
            'user': userprofile,
            'list': list
        }
    else:
        context = {
            'blogs': blogs,
            'tags': request_tag,
        }
    return render(request, 'core/tag.html', context)