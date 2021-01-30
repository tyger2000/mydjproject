from django.db import models

# Create your models here.
class blog_project(models.Model):
	title = models.CharField(max_length=30)
	description = models.CharField(max_length= 200)
	date = models.DateField()
	text = models.TextField(max_length=400)