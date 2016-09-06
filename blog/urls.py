from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^contact.html/$', views.contactus, name='contactus'),
    url(r'^about.html/$', views.about, name='about'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
