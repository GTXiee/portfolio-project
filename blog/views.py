from django.shortcuts import render, get_object_or_404

from .models import Post


def allblogs(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'blog/allblogs.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
