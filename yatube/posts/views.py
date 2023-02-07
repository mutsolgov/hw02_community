from django.shortcuts import render, get_object_or_404

from .models import Post, Group

TEN = 10

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:TEN]
    context = {'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:TEN]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
