from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name=
    url(r'', include('webmaster_verification.urls')),
    url(r'', include('blog.urls')),
    url(r'^djga/', include('google_analytics.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
