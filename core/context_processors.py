from .forms import NewsletterForm

def newsletter(request):
	nf = NewsletterForm()
	context = {
		'nf': nf
	}
	return context