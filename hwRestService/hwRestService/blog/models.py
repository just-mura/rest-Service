from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author    = models.CharField(max_length = 30)
	title     = models.CharField(max_length = 30)
	text      = models.CharField(max_length = 100)
	pub_date  = models.DateTimeField(auto_now_add = True)
	upd_date  = models.DateTimeField(auto_now = True)
	is_public = models.BooleanField(default = True)

class Comment(models.Model):
	author    = models.CharField(max_length = 30)
	text      = models.CharField(max_length = 100)
	pub_date  = models.DateTimeField(auto_now_add = timezone.now)
	post      = models.ForeignKey(Post)	