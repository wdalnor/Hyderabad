from django.conf.urls import url
from . import views


urlpatterns = [


    url(r'^show/(?P<notification_id>\d+)/$', views.show_notification, name='show_notification'),
    url(r'^delete/(?P<notification_id>\d+)/$', views.delete_notification, name='delete_notification'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^popupform/$', views.popupform, name='popupform'),
    url(r'^addnote/$', views.addnote, name = 'addnote'),
    url(r'^time/$', views.current_datetime, name ='time'),
]









        
