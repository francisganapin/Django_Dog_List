from django.urls import path
from .views import dog_views,about_views
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns =[
    
    path('',dog_views,name='dog_views'),
    path('about',about_views,name='about_views'),
    path('dog/<str:breed_name>/',views.dog_detail,name='dog_detail'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
