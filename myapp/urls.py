from django.urls import path
from . import views
urlpatterns = [
    path('hello',views.hello,name = "hello"),
    path('world',views.world,name = "world"),
    path('indexf',views.indexf,name = "indexf"),
   
]

