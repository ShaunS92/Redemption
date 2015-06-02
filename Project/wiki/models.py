from django.db import models
from django.utils import timezone

class Category(models.Model):
	category_title = models.CharField(max_length='140',default="New Category")

	def __str__(self):
		return self.category_title
	
class Article(models.Model):
	article_title = models.TextField(max_length='140',default="New Article")
	article_content = models.TextField(max_length='140',default="New Article",null=True)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.article_title

class Article_Content_History (models.Model):
	article_author_id = models.TextField(default='Empty',null=True)
	article_author = models.TextField(default='Empty',null=True)
	article_content_history=models.TextField(default='Empty',null=True)
	article_related = models.TextField(default='Empty',null=True)
	article_content_history_timestamp = models.DateTimeField('Timestamp',default=timezone.now())
	
	def __str__(self):
		return self.article_content_history_timestamp
