from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import News, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .forms import UserRegisterForm, UserLoginForm, NewsForm, CommentForm
from django.contrib.auth import login, logout
from django.contrib import messages


class AllNews(ListView):
    model = News
    template_name = 'main/index.html'
    context_object_name = 'news_list'
    allow_empty = False
    paginate_by = 10
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['main_news'] = [context['news_list'][item] for item in range(0, 2)]
        except IndexError:
            context['main_news'] = None
        try:
            context['sub_news'] = [context['news_list'][item] for item in range(2, 5)]
        except IndexError:
            context['sub_news'] = None
        return context

    def get_queryset(self):
        return News.objects.all()


class CategoryNews(ListView):
    model = News
    template_name = 'main/genre_news.html'
    context_object_name = 'news_list'
    allow_empty = False
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(pk=self.kwargs['genre_id'])
        context['one_main_news'] = context['news_list'][0]
        context['other_news'] = [context['news_list'][item] for item in range(1, len(context['news_list']))]
        return context

    def get_queryset(self):
        return News.objects.filter(genre_id=self.kwargs['genre_id']).select_related('genre')


# class DetailNews(DetailView):
#     model = News
#     context_object_name = 'one_news'
#     # template_name = 'news/news_detail.html'
#     # pk_url_kwarg = 'news_id'

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    news_item.views += 1
    news_item.save()
    comments = news_item.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news, new_comment.name, new_comment.email = news_item, request.user.username, request.user.email
            new_comment.save()
            return redirect(f'news/{news_id}')
    else:
        comment_form = CommentForm()

    return render(request, 'main/news_detail.html', {
        'one_news': news_item,
        'comments': comments,
        'comment_form': comment_form
    })


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'main/add_news.html'
    login_url = '/admin/'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна')
            return redirect('/news')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/news')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/news/login')

