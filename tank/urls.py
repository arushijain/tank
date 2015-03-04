from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^digitalIndia', views.digitalIndia, name='digitalIndia'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^about', views.about, name='about'),
    #url(r'^createIssue', views.IssueCreateView.as_view() , name='createIssue'),
    url(r'^createIssue', views.createIssue , name='createIssue'),
    url(r'^viewtickets', views.viewTickets, name='viewTickets'),
    url(r'^project', views.project, name='project'),
#     url(r'^facebook/', include('django_facebook.urls')),
#     url(r'^accounts/', include('django_facebook.auth_urls')),  #Don't add this line if you use django registration or userena for registration and auth.
# )
)
