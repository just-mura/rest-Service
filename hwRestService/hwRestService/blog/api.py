from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from hwRestService.blog import models
from tastypie.authorization import Authorization
from tastypie import fields

class PostResource(ModelResource):
	author = fields.CharField(attribute="author")
	text = fields.CharField(attribute="text")
	title = fields.CharField(attribute="title")
    #is_public = fields.BooleanField(attribute="is_public",use_in="detail")
	Comment = fields.ToManyField('hwRestService.blog.api.CommentResource','comment_set', null=True,use_in="detail")
	class Meta:
		queryset = models.Post.objects.all()
		resource_name = 'post'
		always_return_data = True
		authorization = Authorization();

class CommentResource(ModelResource):
	#author = fields.CharField(attribute="author")
    #post = fields.ToOneField('hwRestService.blog.api.PostResource', 'post') 
	class Meta:
		queryset = models.Comment.objects.all()
		resource_name = 'comment'
		always_return_data = True
		authorization = Authorization()