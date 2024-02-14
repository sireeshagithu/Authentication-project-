from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import home
from myapp.views import upload_image, register
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),  # Define the root URL pattern
    path('admin/', admin.site.urls),
     path('register/', register, name='register'),
    path('upload/', upload_image, name='upload_image'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
