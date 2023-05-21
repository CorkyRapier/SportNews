from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm, TreadsForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def main_forum(request):
    main_category = Category.objects.all()
    main_treads = MainTreads.objects.all()
    for mtread in main_treads:
        comments_count = 0
        for tread in mtread.treads.all():
            comments_count += len(tread.comments_treads.all())
        mtread.comments_count = comments_count

    return render(request, 'forum/forum.html', {
        'main_category': main_category,
        'main_treads': main_treads
    })

def treads_from_main(request, main_tread_id):
    treads_list = Treads.objects.filter(main_treads=main_tread_id)
    main_tread = MainTreads.objects.get(pk=main_tread_id)

    if request.method == 'POST':
        tread_form = TreadsForm(data=request.POST)
        if tread_form.is_valid():
            new_tread = tread_form.save(commit=False)
            new_tread.main_treads, new_tread.user_id = main_tread, request.user
            new_tread.save()
            return redirect(new_tread)
    
    else:
        tread_form = TreadsForm()

    return render(request, 'forum/detail_main_tread.html', {
        'treads_list': treads_list,
        'main_tread': main_tread,
        'tread_form': tread_form,
    })

def tread_detail(request, main_tread_id, tread_id):
    tread = Treads.objects.get(pk=tread_id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.treads, new_comment.user_id = tread, request.user
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()

    return render(request, 'forum/detail_tread.html', {
        'tread': tread,
        'comment_form': comment_form
    })


def delete_tread(request, main_tread_id, tread_id):
    delete_tread = Treads.objects.get(pk=tread_id)
    delete_tread.delete()
    return redirect(reverse('forum:detail_main', kwargs={"main_tread_id": main_tread_id}))
