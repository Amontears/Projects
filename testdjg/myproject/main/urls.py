# main/urls.py
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news/', include('news.urls')),  # Подключаем URLs из news
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
