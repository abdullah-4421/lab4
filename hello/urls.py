from django.urls import path
from . import views

urlpatterns= [
path("" , views.index2, name ="index"),
path("<str:number>", views.index3, name ="index"),
path("taxrate/" , views.index, name ="index")
]