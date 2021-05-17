from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Tag, Post

def search(request):
	q = request.GET.get('q')
	posts = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(category__title__icontains=q)).distinct()
	tags = Tag.objects.filter(Q(tag__icontains=q))
	context = {
		'posts': posts,
		'tags': tags,
		'q': q
	}
	return render(request, 'blog/search.html', context)

def posts(request):
	posts = Post.objects.all()
	categories = Category.objects.all()
	context = {
		'posts': posts,
		'categories': categories
	}
	return render(request, 'blog/posts.html', context)

def category(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	other_categories = Category.objects.exclude(slug=category_slug)
	context = {
		'category': category,
		'other_categories': other_categories
	}
	return render(request, 'blog/category.html', context)

def tag(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	other_tags = Tag.objects.exclude(slug=tag_slug)
	context = {
		'tag': tag,
		'other_tags': other_tags
	}
	return render(request, 'blog/tag.html', context)

def post(request, category_slug, post_slug):
	post = get_object_or_404(Post, category__slug=category_slug, slug=post_slug)
	related_posts = Post.objects.filter(slug=category_slug)[:3]
	context = {
		'post': post,
		'related_posts': related_posts
	}
	return render(request, 'blog/post.html', context)