from django.conf.urls import patterns, include, url
from django.contrib import admin
from hwRestService.blog.api import PostResource
from hwRestService.blog.api import CommentResource

post_resource = PostResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hwRestService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(post_resource.urls)),
    (r'^api/v1/', include(comment_resource.urls)),
)
