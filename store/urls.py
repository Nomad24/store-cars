from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('car/<str:slug>/', GetPost.as_view(), name='car'),
    path('search/', Search.as_view(), name='search'),
    path('add_cars/', CreateCars.as_view(), name='add_cars')
]