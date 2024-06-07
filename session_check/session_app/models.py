from django.db import models

# Create your models here.
class Author (models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField()

class Book (models.Model):
    title = models.CharField()
    summary = models.TextField()
    author = models.ForeignKey(Author, on_delete= models.CASCADE)