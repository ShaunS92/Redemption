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
	print(test)
	articles = Article.objects.filter(category_id=test)
	context = {'articles': articles}
	return render(request, 'wiki/category.html', context)

def article(request, test):
	thisArticle = Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)


def edit_article_introduction(request ,test):
	selected_choice = request.POST.get('intro')
	thisArticle = Article.objects.get(id=test)
	thisArticle.article_introduction =selected_choice
	thisArticle.save()

	thisArticle=Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)



def edit_article_rating(request ,test):
	print("Rating")
	selected_choice = request.POST.get('rat')
	articleToEdit = Article.objects.get(id=test)
	articleToEdit.article_rating =selected_choice
	articleToEdit.save()
	
	thisArticle=Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)

def edit_article_soil(request ,test):
	selected_choice = request.POST.get('sol')
	articleToEdit = Article.objects.get(id=test)
	articleToEdit.article_soil =selected_choice
	articleToEdit.save()

	thisArticle=Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)

def edit_article_sunlight(request ,test):
	selected_choice = request.POST.get('sun')
	articleToEdit = Article.objects.get(id=test)
	articleToEdit.article_sunlight =selected_choice
	articleToEdit.save()

	thisArticle=Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)

def edit_article_watering(request ,test):
	selected_choice = request.POST.get('wat')
	articleToEdit = Article.objects.get(id=test)
	articleToEdit.article_watering =selected_choice
	articleToEdit.save()

	thisArticle=Article.objects.get(id=test)
	context = {'thisArticle': thisArticle}
	return render(request, 'wiki/article.html',context)