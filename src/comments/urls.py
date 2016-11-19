from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import (
	comment_thread,
	comment_delete,

	)

urlpatterns = patterns('',
  url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
  url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),

)

# from .views import (
# 	post_create,
# 	post_detail,
# 	post_list,
# 	post_update,
# 	post_delete,
# 	)

# urlpatterns = patterns('',
#   url(r'^create/$', "post_create"),
#   url(r'^detail/(?P<id>\d+)/$', "post_detail"),
#   url(r'^$', "post_list"),
#   url(r'^update/$', "post_update"),
#   url(r'^delete/$', "post_delete"),

# )
