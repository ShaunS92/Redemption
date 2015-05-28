from django.conf.urls import url
from . import views

urlpatterns = [ 
	
	url(r'^$',views.wiki, name='wiki'), 
	url(r'^Categories/',views.categories, name='categories'),
	url(r'^Category/?(?P<test>\w?/?)/',views.category, name='category'),
	url(r'^Article/?(?P<test>\w?/?)/',views.article, name='article'),
	url(r'^123/?(?P<test>\w?/?)/123',views.edit_article_introduction, name='edit_article_introduction'),
	url(r'^1231/?(?P<test>\w?/?)123/',views.edit_article_rating, name='edit_article_rating'),
	url(r'^12323/?(?P<test>\w?/?)123/',views.edit_article_soil, name='edit_article_soil'),
	url(r'^12334/?(?P<test>\w?/?)123/',views.edit_article_sunlight, name='edit_article_sunlight'),
	url(r'^12345/?(?P<test>\w?/?)123/',views.edit_article_watering, name='edit_article_watering'),

	#url(r'^',views.category, name='category'),
	#url(r'^',views.article, name='article'),
	

	#url(r'^x/Basil/', views.view_article, name='view_article'),
	#url(r'^Category/(?P<article_title>)', views.view_article, name='view_article'),
	#url(r'^Category/([A-Za-z]+)/(?P<article_title>)', views.view_article, name='view_article'),
	
	
	


	
]
