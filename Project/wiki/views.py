from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from wiki.models import Category
from wiki.models import Article

def wiki(request):
	return render(request, 'wiki/wiki.html')

def view_categories(request):
	display_categories = Category.objects.all()
	context = {'display_categories': display_categories}
	return render(request, 'wiki/categories.html', context)

def view_category(request, category_title):
	display_category = Article.objects.all()
	context = {'display_category': display_category}
	return render(request, 'wiki/category.html',context)

def view_article(request):
	display_article = Article.objects.all()
	context = {'display_article': display_article}
	return render(request, 'wiki/article.html', context)


