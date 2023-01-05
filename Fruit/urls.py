from django.contrib import admin
from django.urls import path
from Fruit import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.hilo,name="hel"),
    path('res/',views.fruitmodel,name="res"),
    path('image_upload/', hotel_image_view, name='image_upload'),
    path('success/', success, name='success'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)