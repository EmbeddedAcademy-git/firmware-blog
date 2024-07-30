from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.blog_view, name='blog_view'),
    #path('<str:author>/', views.author_blogs, name='author_blogs'),
]
