from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MainTreads(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главный тред"
        verbose_name_plural = "Главные треды"
        ordering = ['-date_create']

    def get_absolute_url(self):
        return reverse('forum:detail_main', kwargs={"main_tread_id": self.pk})


class Treads(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    main_treads = models.ForeignKey(MainTreads, related_name='treads', on_delete=models.CASCADE, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тред"
        verbose_name_plural = "Треды"
        ordering = ['-date_create']

    def get_absolute_url(self):
        return reverse('forum:one_tread', kwargs={"tread_id": self.pk, "main_tread_id": self.main_treads.pk})


class Comments(models.Model):
    user_id = models.ForeignKey(User, related_name='user_treads', on_delete=models.CASCADE, null=True, blank=True)
    treads = models.ForeignKey(Treads, related_name='comments_treads', on_delete=models.CASCADE, null=False, blank=False)
    comment_text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user_id} on {self.treads}'
