from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(editable=False, max_length=130)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ('-id', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:category', kwargs={
				'category_slug': self.slug
			})

class Tag(models.Model):
	tag = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(editable=False, max_length=130)

	def __str__(self):
		return self.tag

	class Meta:
		ordering = ('-id', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.tag)
		super(Tag, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:tag', kwargs={
				'tag_slug': self.slug
			})

class Post(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(editable=False, max_length=130)
	thumbnail = models.ImageField(upload_to='blog/thumbnails/')
	alt_tag_thumbnail = models.CharField(max_length=50, null=True, blank=True)
	banner = models.ImageField(upload_to='blog/banners/')
	alt_tag_banner = models.CharField(max_length=50, null=True, blank=True)
	content = RichTextUploadingField()
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	tags = models.ManyToManyField(Tag)
	seo_title = models.CharField(max_length=120, null=True, blank=True)
	seo_description = models.CharField(max_length=200, null=True, blank=True)
	seo_tags = models.TextField(null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-created_on', )

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('blog:post', kwargs={
				'category_slug': self.category.slug,
				'post_slug': self.slug
			})