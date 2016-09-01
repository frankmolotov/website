from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from .models import Post
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
    width = int(request.device.width)
    height = int(request.device.height)
    multiplier = float(width)/height
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegisterForm()
    return render(request, 'blog/base.html', {'form': form, 'multiplier': multiplier}, context_instance=RequestContext(request))
