from django.conf.urls import url
from . import views

urlpatterns = [ 
	
	url(r'^$',views.wiki, name='wiki'), 
	url(r'^Categories/',views.categories, name='categories'),
	url(r'^Category/?(?P<test>\w+/?)/',views.category, name='category'),
	url(r'^Article/?(?P<test>\w+?/?)/',views.article, name='article'),
	url(r'^Edit/(?P<eai>\w+)/',views.edit_article_content, name='edit_article_content'),
	
	url(r'^History/(?P<hai>\w+)/',views.article_history, name='article_history'),
	url(r'^Content Reverted/(?P<ri>\w+)/(?P<related>\w+)',views.revert_content, name='revert_content'),
	


	url(r'^Add Category/',views.add_category, name='add_category'),
	url(r'^Add Article/(?P<categoryID>\w+)/',views.add_article, name='add_article'),
	#url(r'^',views.category, name='category'),
	#url(r'^',views.article, name='article'),
	

	#url(r'^x/Basil/', views.view_article, name='view_article'),
	#url(r'^Category/(?P<article_title>)', views.view_article, name='view_article'),
	#url(r'^Category/([A-Za-z]+)/(?P<article_title>)', views.view_article, name='view_article'),
	
	
	


	
]

