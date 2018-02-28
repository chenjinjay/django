"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from article import views as article_views
from login import views as login_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', article_views.home, name = 'home'),
    url(r'^(?P<my_args>\d+)/$',article_views.detail,name = 'detail'),
    url(r'^login/$',login_views.login,name = 'login'),
    url(r'^regist/$',login_views.regist,name = 'regist'),
    url(r'^login/init/$',login_views.index,name = 'init'),
    url(r'^logout/$',login_views.logout,name = 'logout'),
    url(r'^index',article_views.person,name='index'),
] 
