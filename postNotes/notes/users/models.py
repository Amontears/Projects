from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_images')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Сначала сохраняем объект, чтобы убедиться, что файл загружен
        super().save(*args, **kwargs)

        # Если есть аватар, изменим его размер
        if self.avatar:
            try:
                # Проверяем путь к изображению
                img_path = self.avatar.path
                if os.path.exists(img_path):
                    img = Image.open(img_path)

                    # Проверка, если размер изображения превышает допустимые параметры
                    if img.height > 250 or img.width > 250:
                        new_img = (250, 250)  # Максимальный размер 250x250
                        img.thumbnail(new_img)  # Изменяем размер изображения
                        img.save(img_path)  # Сохраняем изменённое изображение
                else:
                    print(f"File {img_path} does not exist")  # Логирование, если файл не найден
            except Exception as e:
                print(f"Error resizing image: {e}")
