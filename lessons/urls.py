from django.urls import path,include
from . import views  # Import your views

urlpatterns = [
    # For regular views, like rendering a template
    path('', views.lesson_list, name='lesson_list'),  # You can use a normal view here

    # If you're adding the API URLs for the 'lessons' app:
    path('api/', include('api.urls')),  # API is already configured in api/urls.py
]
