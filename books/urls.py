from django.conf.urls import url
from . import views
from django.conf import settings

app_name = 'books'


urlpatterns = [

    url(r'^$', views.books_list, name='book_list'),
    url(r'^search/$', views.search, name='search'),
    url(r'^login/$', views.userlogin, name='user_login'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.login, name='login'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^detail/(?P<id>\d+)/$', views.book_detail, name='detail'),
    url(r'^like/(?P<book_id>\d+)/$', views.like_this_book, name ='like_this_book'),
    url(r'^update_book/(?P<book_id>\d+)/$', views.update_book, name='update_book'),
    url(r'^delete_book/(?P<book_id>\d+)/$', views.conform_delete, name='conform_delete'),
    url(r'register/$', views.register, name='register'),


]



#if settings.DEBUG:
#  urlpatterns +=[url(r'^debuginfo/$', views.debug),]
