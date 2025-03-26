from django.urls import path
from sistema import views

urlpatterns = [

    path('painel', views.home_admin, name='home_admin'),
    path('painel/user', views.home_user, name='home_user'),
]