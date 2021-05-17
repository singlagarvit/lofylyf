from django.contrib import admin
from .models import Category, Tag, Post

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']

class TagAdmin(admin.ModelAdmin):
	list_display = ['tag', 'slug']

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'category', 'created_on']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)