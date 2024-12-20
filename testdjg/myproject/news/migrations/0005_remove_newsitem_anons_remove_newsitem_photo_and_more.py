# Generated by Django 5.1.4 on 2024-12-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsitem_remove_articles_anons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='anons',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='photo',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='image',
            field=models.ImageField(default='', upload_to='news_images/'),
            preserve_default=False,
        ),
    ]