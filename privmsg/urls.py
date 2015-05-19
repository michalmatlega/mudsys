from django.conf.urls import patterns, url
 
from privmsg import views
 
urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<chat_room_id>\d+)/$', views.chat_room, name='chat_room'),
    #url(r'^(?P<chat_room_id>\d+)/reply/$', views.reply, name='reply'),

    #url(r'^$', views.index, name='index'),
    url(r'^(?P<msg_id>\d+)/show/$', views.show, name='show'),
    url(r'^outbox/$', views.outbox, name='outbox'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^send/$', views.send, name='send'),
    url(r'^(?P<msg_id>\d+)/reply/$', views.reply, name='reply'),
)