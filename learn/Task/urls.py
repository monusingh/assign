from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
           
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$',  logout),
    url(r'^$', 'Record.views.getMovies'),
    url(r'^home', 'Record.views.home'),
    url(r'^', include('favorites.urls', app_name='favorites', namespace="favorites")),
   
)
