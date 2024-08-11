from django.db import models

# Create your models here

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title , self.author, self.publication_year

class Arthur(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    