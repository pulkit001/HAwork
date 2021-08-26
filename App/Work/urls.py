from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index) ,path('lost' , views.LostL) ,path('found' , views.FoundL) , path('Lost/<item>' , views.lostD) , path('Found/<item>' , views.foundD ),
    path('LostForm' , views.lost) , path('FoundForm' , views.found)
]
