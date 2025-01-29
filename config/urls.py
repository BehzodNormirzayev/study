from django.contrib import admin
from django.urls import path, include  # Make sure you include the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the 'api/urls.py' here
]
