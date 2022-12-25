from django.urls import path
from dreams import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='О нас'),
    path('contact', views.contact, name='Контакты')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)