from django.urls import path
from . import views

urlpatterns = [
    path('',views.abc,name='world'),
    path('add',views.add,name='add') #function should exist in view 
]



