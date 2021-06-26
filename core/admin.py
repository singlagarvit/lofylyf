from django.contrib import admin
from .models import Query, Newsletter, MetaTag

class QueryAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'received_on']

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['email']

class MetaTagAdmin(admin.ModelAdmin):
	list_display = ['page', 'name', 'content']

admin.site.register(Query, QueryAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(MetaTag, MetaTagAdmin)