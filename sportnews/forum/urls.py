from django.urls import path
from .views import *


app_name = 'forum'

urlpatterns = [
    path('', main_forum, name='all_treads'),
    path('<int:main_tread_id>/', treads_from_main, name='detail_main'),
    path('<int:main_tread_id>/<int:tread_id>', tread_detail, name='one_tread'),
    path('<int:main_tread_id>/delete/<int:tread_id>', delete_tread, name='delete_tread')
]