from django.urls import path
from .views import BlogAPIView, BloagDetailGenericView


urlpatterns = [
    path('blog/', BlogAPIView.as_view()),
    path('blog/<int:pk>/', BloagDetailGenericView.as_view()),
]