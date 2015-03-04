from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^digitalIndia', views.collapsibleTreeMap, name='digitalIndia'),
    url(r'^signup', views.signup, name='signup'),
    
)
