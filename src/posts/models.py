from __future__ import unicode_literals
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from comments.models import Comment
# from django.db.models.signals import pre_save
# from django.utils.text import slugify

 


class  PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(drafts=False).filter(publish__lte=timezone.now())

def upload_location(instance , filename):
	filebase, extension = filename.split(".")
	return "%s/%s" %(instance.id , filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=20)
	# slug = models.SlugField(unique=True)
	image = models.ImageField(null=True, blank=True, height_field="height", width_field="width",upload_to = upload_location)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	width = models.IntegerField(default=100)
	height = models.IntegerField(default=100)
	content = models.TextField()
	drafts = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False,auto_now_add=False)
	# read_time = models.TimeField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	objects = PostManager()
	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
		# return "/posts/%s/" %(self.id)


	class Meta:
		ordering =["-timestamp", "-updated"]

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)
		

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs


	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type
	




# Recursive function
# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.title)
# 	if new_slug is not None:
# 		slug = new_slug
# 	qs = Post.objects.filter(slug=slug).order_by("-id")
# 	exists = qs.exists()
# 	if exists:
# 		new_slug = "%s-%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug



# def pre_save_post_receiver(sender, instance, *args, **kwargs):
# 	# slug = slugify(instance.title)
# 	# exists = Post.objects.filter(slug=slug).exists()
# 	# if exists:
# 	# 	slug = "%s-%s" %(slug, instance.id)
# 	# instance.slug = slug
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)
	



# pre_save.connect(pre_save_post_receiver, sender=Post)

