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
    path("", views.image_view, name="image_upload"),
    path("success/", views.success, name='success'),
    path('images/', views.encoded_image_view, name = 'images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)