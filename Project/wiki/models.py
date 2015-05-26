from django.db import models

class Category(models.Model):
	category_title = models.CharField(max_length='140',default="New Category")

	def __str__(self):
		return self.category_title


class Article(models.Model):
	article_title = models.CharField(max_length='140',default="New Article")
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.article_title
