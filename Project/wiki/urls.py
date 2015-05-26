from django.conf.urls import url
from . import views

urlpatterns = [ 
	
	
	url(r'^Categories/$',views.view_categories, name='view_categories'),
	url(r'^Categories/(?P<category_title>)',views.view_category, name='view_category'),
	url(r'^Categories/Herbs/',views.view_article, name='view_article'),
	#url(r'^x/Basil/', views.view_article, name='view_article'),
	#url(r'^Category/(?P<article_title>)', views.view_article, name='view_article'),
	#url(r'^Category/([A-Za-z]+)/(?P<article_title>)', views.view_article, name='view_article'),
	
	url(r'^$',views.wiki, name='wiki'),  
	


	
]
