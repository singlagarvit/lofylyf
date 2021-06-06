from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class CoreSitemap(Sitemap):
	priority = 1
	changefreq = 'daily'

	def items(self):
		return [
		'core:index',
		'core:about',
		'core:contact'
		]

	def location(self, item):
		return reverse(item)