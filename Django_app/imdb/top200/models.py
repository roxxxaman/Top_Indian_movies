from django.db import models

# Create your models here.
class Movies(models.Model):
	title=models.CharField(max_length = 250)
	crew=models.TextField(null=True)
	director = models.CharField(max_length = 250, blank=True)
	cast = models.CharField(max_length = 300, null=True)
	year = models.CharField(max_length = 50)
	rating = models.CharField(max_length = 50)
	language = models.CharField(max_length = 50)
