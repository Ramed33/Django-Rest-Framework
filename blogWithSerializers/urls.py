from django.contrib import admin 
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
