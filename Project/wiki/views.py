from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from wiki.models import Category
from wiki.models import Article

def wiki(request):
	return render(request, 'wiki/wiki.html')

def categories(request,):
	categories = Category.objects.all()
	context = {'categories': categories}
	return render(request, 'wiki/categories.html',context)

def category(request, test):
	articles = Article.objects.filter(category_id=test)
	context = {'articles': articles}
	return render(request, 'wiki/category.html', context)

def article(request):
	return render(request, 'wiki/article.html')


