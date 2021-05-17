from django.contrib import admin
from .models import Query, Newsletter

class QueryAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'received_on']

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['email']

admin.site.register(Query, QueryAdmin)
admin.site.register(Newsletter, NewsletterAdmin)