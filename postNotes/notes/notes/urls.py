from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('', include('noteapp.urls')),  # Основные маршруты вашего приложения
    path('users/', include('users.urls')),  # Маршруты для профиля и пользователей

    # Маршруты для аутентификации, можно оставить по умолчанию
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Страница логина
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница логаута
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  # Страница изменения пароля
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),  # Страница после изменения пароля
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Страница сброса пароля
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Страница после запроса на сброс пароля
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Страница для подтверждения сброса пароля
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Страница после завершения сброса пароля
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Статические и медиафайлы для разработки
