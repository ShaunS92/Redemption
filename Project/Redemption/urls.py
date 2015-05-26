from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls', namespace="home")),	
    url(r'^wiki/', include('wiki.urls', namespace="wiki")),	
]
