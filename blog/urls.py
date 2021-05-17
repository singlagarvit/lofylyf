from django.urls import path
from .views import search, posts, category, tag, post
app_name = 'blog'

urlpatterns = [
	path('search/', search, name='search'),
	path('posts/all/', posts, name='posts'),
	path('category/<slug:category_slug>/', category, name='category'),
	path('tag/<slug:tag_slug>/', tag, name='tag'),
	path('<slug:category_slug>/<slug:post_slug>/', post, name='post'),
]