from django.urls import path
from . import views

urlpatterns = [
    path('<id>/', views.blog_view, name='blog_view'),
]
