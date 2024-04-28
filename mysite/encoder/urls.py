from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from encoder.views import home
import encoder.views as views
from django.views.generic.base import RedirectView

urlpatterns = [
    #path("",),
    path("image_upload/", views.image_view, name="image_upload"),
    path("success/", views.success, name='success'),
    path('images/', views.encoded_image_view, name = 'images'),
    path('encoder/', home, name='home'),  # Set this as the homepage
    path('decoder/', include('decoder.urls')),  # Assuming decoder URLs are still relevant
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)