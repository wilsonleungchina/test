#from django.conf.urls import url 
from django.urls import re_path as url
from . import views 
from django.contrib.auth import login

urlpatterns = [ 
 # ึ๗าณ
url(r'^$', views.index, name='index'), 
url(r'^topics/$', views.topics, name='topics'),
url(r'^topics/(?P<topic_ids>\d+)/$', views.topic, name='topic'),
url(r'^new_topic/$', views.new_topic, name='new_topic'),
url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,name='new_entry'),
url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]