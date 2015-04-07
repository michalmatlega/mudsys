from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mudsys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
     url(r'^chats/', include('chat.urls', namespace='chat')),
     url(r'^admin/', include(admin.site.urls)),
)
