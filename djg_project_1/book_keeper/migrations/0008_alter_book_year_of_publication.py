# Generated by Django 5.1.7 on 2025-03-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_keeper', '0007_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.CharField(max_length=5),
        ),
    ]
