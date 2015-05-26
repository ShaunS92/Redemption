from django.db import models
from django.utils import timezone

class Category(models.Model):
	category_title = models.CharField(max_length='140',default="New Category")

	def __str__(self):
		return self.category_title
	
class Article(models.Model):
	article_title = models.CharField(max_length='140',default="New Article")
	category = models.ForeignKey(Category)
	article_text = models.TextField(default='add content here')
	article_editors = models.CharField(max_length='200', default='edited by')
	pub_date = models.DateTimeField('date published', default=timezone.now())
	def __str__(self):
		return self.article_title
