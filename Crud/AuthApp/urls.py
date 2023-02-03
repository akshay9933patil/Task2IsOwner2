from django.urls import path
from .views import UserAPIVIew


urlpatterns = [
    path('user/', UserAPIVIew.as_view())
]