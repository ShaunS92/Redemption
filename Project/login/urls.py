from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^login/', 'login.views.login_view', name='login'),
	url(r'^logout/', 'login.views.logout_view', name='logout'),
	url(r'^register/', 'login.views.register_view', name='register'),
	]