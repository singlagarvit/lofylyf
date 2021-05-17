from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import QueryForm, NewsletterForm
from blog.models import Post, Category

def index(request):
	latest_posts = Post.objects.all()[:3]
	featured_posts = Post.objects.filter(featured=True)[:3]
	featured_categories = Category.objects.filter(featured=True)
	context = {
		'latest_posts': latest_posts,
		'featured_posts': featured_posts,
		'featured_categories': featured_categories
	}
	return render(request, 'core/index.html', context)

def about(request):
	return render(request, 'core/about.html')

def contact(request):
	form = QueryForm(label_suffix='')
	if request.method == 'POST':
		form = QueryForm(request.POST, label_suffix='')
		if form.is_valid():
			form.save()
			return redirect('core:index')
	context = {
		'form': form
	}
	return render(request, 'core/contact.html', context)

@require_POST
def subscribe(request):
	form = NewsletterForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('core:index')
	return None