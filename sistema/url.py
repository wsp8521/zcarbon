from django.urls import path
from sistema import views

urlpatterns = [


    #CRUD desh
    path('sistema', views.home, name='home_sistema'),
]