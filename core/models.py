from django.db import models

PAGE_CHOICES = (
	('index', 'home'),
	('about', 'about'),
	('contact', 'contact'),
)

class Query(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=120, null=True, blank=True)
	message = models.TextField()
	received_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-received_on', )
		verbose_name_plural = 'Queries'

class Newsletter(models.Model):
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.email

class MetaTag(models.Model):
	page = models.CharField(max_length=7, choices=PAGE_CHOICES)
	name = models.CharField(max_length=20)
	content = models.TextField()

	def __str__(self):
		return self.name