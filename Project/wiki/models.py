from django.db import models

class Category(models.Model):
	category_title = models.CharField(max_length='140',default="New Category")

	def __str__(self):
		return self.category_title
	
class Article(models.Model):
	article_title = models.CharField(max_length='140',default="New Article")
	
	article_introduction = models.CharField(max_length='140',default="New Article",null=True)

	article_rating = models.TextField(default='No rating yet')

	article_soil = models.TextField(default='No information on soil added yet! Be the fisrt to post something!')
	article_sunlight = models.TextField(default='No information on sunlight added yet! Be the fisrt to post something!')
	article_watering = models.TextField(default='No information on watering added yet! Be the fisrt to post something!')

	category = models.ForeignKey(Category)

	def __str__(self):
		return self.article_title