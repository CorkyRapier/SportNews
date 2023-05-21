from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-date_create']

    def get_absolute_url(self):
        return reverse('main:genre_news', kwargs={"genre_id": self.pk})


class News(models.Model):
    title = models.CharField(max_length=255)
    news_text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('main:detail', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date_create']


class Comments(models.Model):
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, null=False, blank=False)
    comment_text = models.TextField()
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name if self.name else self.user_id} on {self.news}'
