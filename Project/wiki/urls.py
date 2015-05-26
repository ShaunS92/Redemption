from django.conf.urls import url
from . import views

urlpatterns = [ 
	
	url(r'^$',views.wiki, name='wiki'), 
	url(r'^Categories/',views.categories, name='categories'),
	url(r'^Category/?(?P<test>\w?/?)',views.category, name='category'),
	url(r'^Article/',views.article, name='article'),
	#url(r'^',views.category, name='category'),
	#url(r'^',views.article, name='article'),
	

	#url(r'^x/Basil/', views.view_article, name='view_article'),
	#url(r'^Category/(?P<article_title>)', views.view_article, name='view_article'),
	#url(r'^Category/([A-Za-z]+)/(?P<article_title>)', views.view_article, name='view_article'),
	
	
	


	
]
