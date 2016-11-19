from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views

urlpatterns = patterns('',
  url(r'^create/$', "posts.views.post_create"),
  url(r'^(?P<id>\d+)/$', "posts.views.post_detail", name='detail'),
  url(r'^$', "posts.views.post_list", name='list'),
  url(r'^(?P<id>\d+)/edit/$', "posts.views.post_update"),
  url(r'^(?P<id>\d+)/delete/$', "posts.views.post_delete"),

)

# from .views import (
# 	post_create,
# 	post_detail,
# 	post_list,
# 	post_update,
# 	post_delete,
# 	)

# urlpatterns = patterns('',
#   url(r'^$', post_list, name='list'),
#   url(r'^create/$', post_create),
#   url(r'^(?P<slug>[\w-]\+)/$', post_detail, name='detail'),

#   url(r'^(?P<slug>[\w-]\+)/edit/$', post_update, name='update'),
#   url(r'^(?P<slug>[\w-]\+)/delete/$', post_delete),

# )
