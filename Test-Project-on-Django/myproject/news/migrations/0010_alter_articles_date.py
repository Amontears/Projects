# Generated by Django 5.1.4 on 2024-12-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_articles_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]
