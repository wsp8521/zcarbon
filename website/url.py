from django.urls import path
from website import views

urlpatterns = [
    #w
    path('', views.home, name='home'),
]