from django.urls import include
from django.urls import re_path as url
from django.contrib import admin 
from . import views
from django.contrib.auth.views import LoginView
app_name = 'users'
urlpatterns = [
    #��¼����  LoginView.as_view����Ҫ����()
    #url(r'^login/$', login,{'template_name':'users/login.html'}, name='login'),
    url(r'^login/$',LoginView.as_view(template_name = 'users/login.html'),name='login'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^register/$',views.register,name='register'),
]
