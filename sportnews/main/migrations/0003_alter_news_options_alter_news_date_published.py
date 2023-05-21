# Generated by Django 4.2 on 2023-05-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_create'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='date_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
