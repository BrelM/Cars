from django.urls import path
from .views import UserView

from . import views

urlpatterns = [
    path('Users/', UserView.as_view()),
    path('Users/<int:pk>/', UserView.as_view()),
]
