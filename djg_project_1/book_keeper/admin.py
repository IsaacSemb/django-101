from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Book)

notes = """

changing the string representation of objects to show title in admin
You overide the __str__ method in the model


"""
