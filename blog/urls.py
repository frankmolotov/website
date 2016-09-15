from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^contact.html/$', views.contactus, name='contactus'),
    url(r'^about.html/$', views.about, name='about'),
]
