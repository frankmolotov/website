from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .forms import RegisterForm
from .models import Count
from django.http import HttpResponseRedirect
from django.template import RequestContext

'''def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})
'''


def contact(request):
    if request.method == 'POST':
        count = Count.objects.get(id=1)
        count.count_of_users = str(int(count.count_of_users) + 1)  # change field
        count.save()
        form = RegisterForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.registration_date = timezone.now()
            contact.save()
            return render(request, 'blog/thanks.html', {'username': form['user_name'].value()})
    else:
        form = RegisterForm()
    return render(request, 'blog/index.html', {'form': form, 'count_of_users': Count.objects.all()[0].count_of_users, 'total_capital': Count.objects.all()[0].capital})

def thanks(request):
    return render(request, 'blog/thanks.html')


def contactus(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')
