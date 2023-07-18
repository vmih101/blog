from .views import post_like
from django.urls import path

urlpatterns = [
    path('', post_like, name='post_like'),
]
