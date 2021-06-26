from .forms import NewsletterForm
from .models import MetaTag

def newsletter(request):
	nf = NewsletterForm()
	context = {
		'nf': nf
	}
	return context

def metatags(request):
	meta_tags = MetaTag.objects.all()
	context = {
		'meta_tags': meta_tags
	}
	return context