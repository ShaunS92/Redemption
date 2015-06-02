from django.contrib import admin
from .models import Category
from .models import Article
from .models import Article_Content_History

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Article_Content_History)

