from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', AllNews.as_view(), name='all_news'),
    path('category/<int:genre_id>/', CategoryNews.as_view(), name='genre_news'),
    path('<int:news_id>/', view_news, name='detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
]