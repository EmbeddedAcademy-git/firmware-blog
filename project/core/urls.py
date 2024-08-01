from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<str:tag>', views.tag, name='tag'),
    #path('author/<str:author>', views.author, name='author'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
]
