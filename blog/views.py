from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Register
from .forms import PostForm, RegisterForm
from django.http import HttpResponseRedirect
from django.template import RequestContext

'''def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})
'''


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return render(request, 'blog/thanks.html', {'username': form['user_name'].value()})
    else:
        form = RegisterForm()
    return render(request, 'blog/index.html', {'form': form})


def thanks(request):
    return render(request, 'blog/thanks.html')

def contactus(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')
