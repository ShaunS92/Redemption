from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import redirect
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

def article(request, test):
	thisArticle = Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)


def edit_article(request ,test):
	selected_choice = request.POST.get('new')
	articleToEdit = Article.objects.get(id=test)
	articleToEdit.article_introduction =selected_choice
	articleToEdit.save()

	articleToEdit=Article.objects.get(id=test)
	context = {'articleToEdit': articleToEdit}
	return HttpResponse("Edit Successful")
