from django import forms
from .models import Query, Newsletter

class QueryForm(forms.ModelForm):
	class Meta:
		model = Query
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(QueryForm, self).__init__(*args, **kwargs)
		self.fields['message'].widget.attrs.update({'class': 'contact__input contact__input--textarea form-control mb-3', 'placeholder': 'Enter your message'})
		for field in self.fields:
			if field != 'message':
				self.fields[field].widget.attrs.update({'class': 'contact__input form-control mb-4', 'placeholder': f'Enter your {field.lower()}'})

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(NewsletterForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your email address'})