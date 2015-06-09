__author__ = 'Krzysiek'

from django.conf.urls import patterns, url

urlpatterns = patterns('taskman.views',
    url(r'^$', 'index', name='index'),
    #url(r'^item_action/(done|delete|onhold)/(\d*)/$', 'item_action'),
    #url(r'^mark_done/(\d*)/$', 'mark_done', name='mark_done'),
)
