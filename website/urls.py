from django.urls import path
from website import views
urlpatterns = [
    path('', views.home, name='home'),
    path('diagnostics', views.diagnostics, name='diagnostics'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]