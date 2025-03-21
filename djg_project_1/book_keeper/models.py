from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    ISBN = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    publisher = models.CharField(max_length=255)
    image_url_sm = models.URLField(max_length=200)
    image_url_md = models.URLField(max_length=200) 
    image_url_lg = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title