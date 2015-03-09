from tastypie.resources import ModelResource
from hwRestService.blog import models
from tastypie.authorization import Authorization


class PostResource(ModelResource):
	class Meta:
		queryset = models.Post.objects.all()
		resource_name = 'post'
		authorization = Authorization();

class CommentResource(ModelResource):
	class Meta:
		queryset = models.Comment.objects.all()
		resource_name = 'comment'
		authorization = Authorization()