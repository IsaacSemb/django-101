from django.db import models

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    publisher = models.CharField(max_length=255)
    image_url_small = models.URLField(max_length=200)
    image_url_medium = models.URLField(max_length=200) 
    image_url_large = models.URLField(max_length=200)