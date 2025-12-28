from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Prefetch
from .models import BlogPost, Comment, Like
from .forms import BlogPostForm


def home(request):
    posts = BlogPost.objects.order_by('-date_added')
    return render(request, 'blogs/home.html', {'posts': posts})

@login_required
def new_post(request):
    form = BlogPostForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.owner = request.user
        post.save()
        messages.success(request, '文章发布成功！')
        return redirect('blogs:home')
    
    return render(request, 'blogs/new_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    
    if request.user != post.owner:
        messages.error(request, '您只能编辑自己的文章！')
        return redirect('blogs:home')
    
    form = BlogPostForm(request.POST or None, instance=post)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, '文章修改成功！')
        return redirect('blogs:home')
    
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    
    if request.user != post.owner:
        messages.error(request, '您只能删除自己的文章！')
        return redirect('blogs:home')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, '文章删除成功！')
        return redirect('blogs:home')
    
    return render(request, 'blogs/delete_post.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(
        BlogPost.objects.select_related('owner')
        .prefetch_related(
            Prefetch('comments', queryset=Comment.objects.filter(is_active=True).select_related('author')),
            'likes'
        ),
        id=pk,
        is_published=True
    )
    
    has_liked = False
    if request.user.is_authenticated:
        has_liked = post.user_has_liked(request.user)
    
    return render(request, 'blogs/post_detail.html', {
        'post': post,
        'has_liked': has_liked
    })