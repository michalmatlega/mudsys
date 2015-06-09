__author__ = 'Krzysiek'

from django.conf.urls import patterns, url
#from fileman import views

urlpatterns = patterns('fileman.views',
                       url(r'^$', 'list', name='list'),
                       url(r'^list/$', 'list', name='list'),
                       )

#urlpatterns = patterns('',
#    url(r'^$', views.list, name='list'),
#    url(r'^list/$', views.list, name='list'),
#)
