from django.urls import path
from .views import current_user, create_user

urlpatterns = [
    path('current_user/', current_user),
    path('register_user/', create_user),
]