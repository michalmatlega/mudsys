from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mudsys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
     #url(r'^(/)?$', include('django.contrib.auth.urls'))
     url(r'^chats/', include('chat.urls', namespace='chat')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/login/$',  'mudsys.views.login'),
    url(r'^accounts/auth/$',  'mudsys.views.auth_view'),    
    url(r'^accounts/logout/$', 'mudsys.views.logout'),
    url(r'^accounts/loggedin/$', 'mudsys.views.loggedin'),
    url(r'^accounts/invalid/$', 'mudsys.views.invalid_login'),
)
