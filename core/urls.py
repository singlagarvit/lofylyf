from django.urls import path
from .views import index, about, contact, subscribe

app_name = 'core'

urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('subscribe/', subscribe, name='subscribe'),
]