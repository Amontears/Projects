from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.news_home, name='news_home'),  # Главная страница новостей
    path('create/', views.create, name='create'),  # Страница создания новости
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
