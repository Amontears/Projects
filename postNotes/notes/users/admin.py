# users/admin.py
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_display')  # Добавьте метод для отображения аватара

    def avatar_display(self, obj):
        return f'<img src="{obj.avatar.url}" width="50" height="50" />'
    avatar_display.allow_tags = True  # Позволяет отображать HTML

# Убедитесь, что только один вызов регистрации
admin.site.register(Profile, ProfileAdmin)
