from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema/', include('sistema.urls')),
    path('', include('website.urls')),
]
