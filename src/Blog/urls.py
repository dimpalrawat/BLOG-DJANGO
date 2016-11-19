from django.conf import settings

from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^posts/$', post_views.post_home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include("comments.urls", namespace='comments')),    
    
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'^', include("posts.urls", namespace='posts')),

    
    )

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
