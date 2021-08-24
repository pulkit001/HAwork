from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index) ,path('lost' , views.lost) ,path('found' , views.found)
]
