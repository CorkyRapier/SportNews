# Generated by Django 4.2 on 2023-04-30 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('news_text', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_published', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre')),
            ],
        ),
    ]
