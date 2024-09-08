from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_year=models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author.name}"


