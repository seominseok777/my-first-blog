from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.post_list, name = 'post_list'),
    url(r'^write$',views.post_writing, name ='post_writing'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name= 'post_detail'),
]
