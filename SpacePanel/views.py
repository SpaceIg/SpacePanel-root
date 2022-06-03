from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return HttpResponse('<h1>Каталог Telegram-каналов и чатов</h1>')

def analytics(request):
	return render(request, 'analytics.html',
	 {'serviceName': 'Аналитика Telegram-каналов и чатов'})

def ratings(request):
	return HttpResponse('<h1>Рейтинг Telegram-каналов</h1>')