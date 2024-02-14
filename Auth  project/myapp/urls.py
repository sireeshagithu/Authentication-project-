from django.urls import path
from .views import upload_image, register

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('register/', register, name='register'),
]
