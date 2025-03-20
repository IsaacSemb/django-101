from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    ISBN = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    year_of_publication = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    image_url_sm = models.URLField(max_length=200)
    image_url_md = models.URLField(max_length=200) 
    image_url_lg = models.URLField(max_length=200)
    # slug = models.SlugField(null=True)
    
    # class Meta:
    #     db_table = 'books'
    #     indexes = [
    #         models.Index( fields=['ISBN'] )
    #         ]