from django.contrib.sitemaps import Sitemap
from blog.models import Category, Tag, Post

class CategorySitemap(Sitemap):
	changefreq = "never"
	priority = 0.6
	protocol = 'https'

	def items(self):
		return Category.objects.all()

class TagSitemap(Sitemap):
	changefreq = "never"
	priority = 0.6
	protocol = 'https'

	def items(self):
		return Tag.objects.all()

class PostSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.5
	protocol = 'https'

	def items(self):
		return Post.objects.all()

	def lastmod(self, obj):
		return obj.created_on