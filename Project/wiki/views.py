from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import redirect
from wiki.models import Category
from wiki.models import Article
from wiki.models import Article_Content_History
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import Image
import imghdr
import os
import os.path






def wiki(request):
	if request.user.is_active:
		try:
				uauth = request.session['auth']
				if (uauth == '0') or (uauth == '1') or (uauth == '2'):
					userid = request.session['user_id']
					fullname = request.session['fullname']
					myuser = User.objects.get(pk=userid)

					userimage = 'wiki/images/' + myuser.username + '.jpeg'
			   		testimage = 'wiki/static/' + userimage
			   		userauth = str(myuser.profile.user_auth)


			   		#VALIDATES FILE EXISTS
			   		if os.path.isfile(testimage) == False:
			   			userimage = 'wiki/images/guest.gif'

					context = {'userauth':userauth,'userauth':userauth,'userid': userid , 'fullname': fullname, 'userimage': userimage }
					return render(request, 'wiki/wiki.html', context)
				else:
					return render(request, 'wiki/wiki.html')

		except KeyError:
			return render(request, 'wiki/wiki.html')
	else:
		return render(request, 'wiki/wiki.html')

def categories(request):

	categories = Category.objects.all()
	context = {'categories': categories }
	if request.user.is_active:
		uauth = request.session['auth']
		if (uauth == '0') or (uauth == '1') or (uauth == '2'):
			try:
				userid = request.session['user_id']
				fullname = request.session['fullname']
				myuser = User.objects.get(pk=userid)
				userauth = str(myuser.profile.user_auth)

				userimage = 'wiki/images/' + myuser.username + '.jpeg'
				
		   		
		   		testuserimage = 'wiki/static/' + userimage
		   		

		   		#VALIDATES FILE EXISTS
		   		if os.path.isfile(testuserimage) == False:
		   			userimage = 'wiki/images/guest.gif'
		   		
				
				context = {'userauth':userauth,'categories': categories, 'userid': userid , 'fullname': fullname,  'userimage': userimage  }
				return render(request, 'wiki/categories.html',context)
			except KeyError:
				return render(request, 'wiki/categories.html',context)
		else:
			return render(request, 'wiki/categories.html', context)
	else:
		return render(request, 'wiki/categories.html', context)

def category(request, test):
	articles = Article.objects.filter(category_id=test)
	thiscat = Category.objects.filter(id=test)[0]
	context = {'articles': articles,'thiscat':thiscat,}
	if request.user.is_active:
		uauth = request.session['auth']
		if (uauth == '0') or (uauth == '1') or (uauth == '2'):
			try:
				userid = request.session['user_id']
				fullname = request.session['fullname']
				myuser = User.objects.get(pk=userid)
				userauth = str(myuser.profile.user_auth)


				userimage = 'wiki/images/' + myuser.username + '.jpeg'
				
		   		
		   		testuserimage = 'wiki/static/' + userimage
		   		

		   		#VALIDATES FILE EXISTS
		   		if os.path.isfile(testuserimage) == False:
		   			userimage = 'wiki/images/guest.gif'
		   		

   			

				context = {'userauth':userauth,'articles': articles,'thiscat':thiscat, 'userid': userid , 'fullname': fullname,  'userimage': userimage  }
				return render(request, 'wiki/category.html', context)

			except KeyError:
				return render(request, 'wiki/category.html', context)
		else:
			return render(request, 'wiki/category.html', context)
	else:
		return render(request, 'wiki/category.html', context)


	

def article(request, test):
	
	thisArticle = Article.objects.get(id=test)
	artimage = 'wiki/images/articles/' + str(thisArticle.id) + '.jpeg'
	testartimage = 'wiki/static/' + artimage
	#VALIDATES FILE EXISTS
   	if os.path.isfile(testartimage) == False:
   		artimage = 'wiki/images/articles/none.jpeg'
	context = {'artimage':artimage,'thisArticle': thisArticle}

	if request.user.is_active:
		uauth = request.session['auth']
		if (uauth == '0') or (uauth == '1') or (uauth == '2'):
			try:
				userid = request.session['user_id']
				fullname = request.session['fullname']
				myuser = User.objects.get(pk=userid)
				userauth = str(myuser.profile.user_auth)

				userimage = 'wiki/images/' + myuser.username + '.jpeg'
				artimage = 'wiki/images/articles/' + str(thisArticle.id) + '.jpeg'
		   		
		   		testuserimage = 'wiki/static/' + userimage
		   		testartimage = 'wiki/static/' + artimage

		   		#VALIDATES FILE EXISTS
		   		if os.path.isfile(testuserimage) == False:
		   			userimage = 'wiki/images/guest.gif'
		   		

   				#VALIDATES FILE EXISTS
   				if os.path.isfile(testartimage) == False:
   					artimage = 'wiki/images/articles/none.jpeg'


				context = {'userauth':userauth,'thisArticle': thisArticle,'userid': userid , 'fullname': fullname  ,'userimage': userimage, 'artimage': artimage   }
				return render(request, 'wiki/article.html',context)
			except KeyError:
				return render(request, 'wiki/article.html',context)
		else:
			return render(request, 'wiki/article.html', context)
	else:
		return render(request, 'wiki/article.html', context)

def edit_article_content(request ,eai):
	thisArticle = Article.objects.get(id=eai)
	context = {'thisArticle': thisArticle}
	if request.user.is_active:
		uauth = request.session['auth']
		if (uauth == '1') or (uauth == '2'):
			try:
				userid = request.session['user_id']
				fullname = request.session['fullname']
				myuser = User.objects.get(pk=userid)
				userauth = str(myuser.profile.user_auth)

				#EDITING
				selected_choice = request.POST.get('intro')
				
				thisArticle.article_content =selected_choice
				thisArticle.save()

				savehistory = Article_Content_History.objects.create(article_author_id=userid, article_author=fullname,article_related=eai, article_content_history=selected_choice)
				savehistory.save()

				thisArticle=Article.objects.get(id=eai)
				#END OF EDITING

				userimage = 'wiki/images/' + myuser.username + '.jpeg'
				artimage = 'wiki/images/articles/' + str(thisArticle.id) + '.jpeg'
		   		
		   		testuserimage = 'wiki/static/' + userimage
		   		testartimage = 'wiki/static/' + artimage

		   		#VALIDATES FILE EXISTS
		   		if os.path.isfile(testuserimage) == False:
		   			userimage = 'wiki/images/guest.gif'
		   		

   				#VALIDATES FILE EXISTS
   				if os.path.isfile(testartimage) == False:
   					artimage = 'wiki/images/articles/none.jpeg'

				context = {'artimage': artimage,'userauth':userauth,'thisArticle': thisArticle,'userid': userid , 'fullname': fullname, 'userimage': userimage,   }
				return render(request, 'wiki/article.html',context)
			except KeyError:
				return render(request, 'wiki/article.html',context)
		else:
			return render(request, 'wiki/article.html', context)
	else:
		return render(request, 'wiki/article.html', context)

#HISTORY
def article_history(request ,hai):
	print("content hist")
	thisArticle=Article.objects.get(id=hai)
	thisHistory = list(Article_Content_History.objects.filter(article_related=hai).order_by('-article_content_history_timestamp')[:5])

	uauth = request.session['auth']
	if (uauth == '0') or (uauth == '1') or (uauth == '2'):
		try:
			userid = request.session['user_id']
			fullname = request.session['fullname']
			myuser = User.objects.get(pk=userid)
			userauth = str(myuser.profile.user_auth)

			userimage = 'wiki/images/' + myuser.username + '.jpeg'
	   		testimage = 'wiki/static/' + userimage
	   		#VALIDATES FILE EXISTS
	   		userimage = 'wiki/images/' + myuser.username + '.jpeg'
			artimage = 'wiki/images/articles/' + str(thisArticle.id) + '.jpeg'
		   		
		   	testuserimage = 'wiki/static/' + userimage
		   	testartimage = 'wiki/static/' + artimage

		   	#VALIDATES FILE EXISTS
		   	if os.path.isfile(testuserimage) == False:
		   		userimage = 'wiki/images/guest.gif'
		   		

   			#VALIDATES FILE EXISTS
   			if os.path.isfile(testartimage) == False:
   				artimage = 'wiki/images/articles/none.jpeg'


			context = {
			'artimage': artimage,
			'userauth':userauth,
			'thisArticle': thisArticle,
			'thisHistory': thisHistory,
			'userid': userid ,
			'fullname': fullname,
		 	'userimage': userimage,
			}
			return render(request, 'wiki/article.html',context)
		except KeyError:
			context = {'thisArticle': thisArticle,
			'thisHistory': thisHistory

			}
			return render(request, 'wiki/article.html',context)
	else:
		context = {'thisArticle': thisArticle,
			'thisHistory': thisHistory

			}
		return render(request, 'wiki/categories.html', context)



##HISTORY REVERT
def revert_content(request ,ri , related):
	thisArticle=Article.objects.get(id=ri)
	history=Article_Content_History.objects.get(id=related)
	 
	thisArticle.article_content = history.article_content_history
	thisArticle.save()

	uauth = request.session['auth']
	if (uauth == '1') or (uauth == '2'):

		try:
			userid = request.session['user_id']
			fullname = request.session['fullname']
			myuser = User.objects.get(pk=userid)
			userauth = str(myuser.profile.user_auth)

			userimage = 'wiki/images/' + myuser.username + '.jpeg'
			artimage = 'wiki/images/articles/' + str(thisArticle.id) + '.jpeg'
		   		
		   	testuserimage = 'wiki/static/' + userimage
		   	testartimage = 'wiki/static/' + artimage

		   	#VALIDATES FILE EXISTS
		   	if os.path.isfile(testuserimage) == False:
		   		userimage = 'wiki/images/guest.gif'
		   		

   			#VALIDATES FILE EXISTS
   			if os.path.isfile(testartimage) == False:
   				artimage = 'wiki/images/articles/none.jpeg'
		
			
			context = {
			'artimage': artimage,
			'userauth':userauth,
			'thisArticle': thisArticle,
			'userid': userid ,
			'fullname': fullname,
			'userimage': userimage,   }

			return render(request, 'wiki/article.html',context)
		except KeyError:
			context = {'thisArticle': thisArticle,
			'thisHistory': thisHistory}
			return render(request, 'wiki/article.html',context)
	else:
		context = {'thisArticle': thisArticle,
			'thisHistory': thisHistory}

			
		return render(request, 'wiki/categories.html', context)

	#ADD

def add_category(request):
	newTitle = request.POST.get('Title')
	newCategory = Category.objects.create(category_title=newTitle)
	newCategory.save()
	categories = Category.objects.all()
	uauth = request.session['auth']
	if (uauth == '1') or (uauth == '2'):
		try:
			userid = request.session['user_id']
			fullname = request.session['fullname']
			myuser = User.objects.get(pk=userid)
			userauth = str(myuser.profile.user_auth)

			userimage = 'wiki/images/' + myuser.username + '.jpeg'
	   		testimage = 'wiki/static/' + userimage
	   		#VALIDATES FILE EXISTS
	   		if os.path.isfile(testimage) == False:
	   			userimage = 'wiki/images/guest.gif'
		
			context = {'userauth':userauth,'categories': categories,'userid': userid ,
			'fullname': fullname,
			'userimage': userimage,   }
			
			return render(request, 'wiki/categories.html',context)
		except KeyError:
			context = {'userauth':userauth,'categories': categories}
			return render(request, 'wiki/categories.html',context)
	else:
		context = {'userauth':userauth,'categories': categories}
		return render(request, 'wiki/categories.html', context)


def add_article(request, categoryID):
	print("Add Article")
	Title = request.POST.get('Title')
	Content = request.POST.get('Content')

	newArticle = Article.objects.create(article_title=Title,article_content=Content,category_id=categoryID)
	newArticle.save()

	if validate_pic(request) == 'nofile':
		load_file =True
	else:
		
		if validate_pic(request) == 'noimage':
			error = 'INVALID FILE'
			context = { 'error': error}
			return render(request, 'wiki/category.html',context)
		else:

			remove_path = 'wiki/static/wiki/images/articles/' + str(newArticle.id) + '.jpeg'
			if os.path.isfile(remove_path):
				os.remove(remove_path)
			new_pic = request.FILES['articlepic']
			default_storage = FileSystemStorage(location='wiki/static/wiki/images/articles/')
			path = default_storage.save(str(newArticle.id) +'.jpeg', ContentFile(new_pic.read()))	
							
	articles = Article.objects.filter(category_id=categoryID)
	thiscat = Category.objects.filter(id=categoryID)[0]
	context = {'articles': articles,'thiscat':thiscat,}

	uauth = request.session['auth']
	if (uauth == '1') or (uauth == '2'):

		try:
			userid = request.session['user_id']
			fullname = request.session['fullname']
			myuser = User.objects.get(pk=userid)
			userauth = str(myuser.profile.user_auth)

			userimage = 'wiki/images/' + myuser.username + '.jpeg'
	   		testimage = 'wiki/static/' + userimage
	   		#VALIDATES FILE EXISTS
	   		if os.path.isfile(testimage) == False:
	   			userimage = 'wiki/images/guest.gif'
		


			context = {'userauth':userauth,'articles': articles,'thiscat':thiscat,'userid': userid ,
			'fullname': fullname,
			'userimage': userimage,
			}
			return render(request, 'wiki/category.html', context)
		except KeyError:
			return render(request, 'wiki/category.html', context)
	else:
		return render(request, 'wiki/category.html', context)



def validate_pic(request):
	try:
		pic =request.FILES['articlepic']  #REQUEST FILE
		file_type = imghdr.what(pic)	#GET IMAGE FILE TYPE
		if file_type == None: #VALIDATE FILE IS AN IMAGE
			return 'noimage'
		else:
			return 'valid'	
	except:
		return 'nofile'