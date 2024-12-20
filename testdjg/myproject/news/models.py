from django.db import models


class Articles(models.Model):
    title = models.CharField('Name_title', max_length=100)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)  # Поле для изображения
    text = models.TextField('Article')
    date = models.DateTimeField('Date')
    
    def __str__(self):
        return f"News : {self.title}"

    def get_absolute_url(self):
        return f"/news/{self.id}"
    


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'