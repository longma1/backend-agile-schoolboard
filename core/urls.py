from django.urls import path
from core.views import current_user, create_user, BoardController

urlpatterns = [
    path('current_user/', current_user),
    path('register_user/', create_user),
    path('board/', BoardController.as_view()),
]