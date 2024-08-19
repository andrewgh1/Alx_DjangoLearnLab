from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "books")

    class Meta:
        permissions = (
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        )


    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library,on_delete=models.CASCADE, related_name="librarians")

    def __str__(self):
        return self.name
    
#Implement Role-Based Access Control (Rbac)
#This code creates the UserProfile model with a one-to-one relationship to the User model 
# and includes a role field. The signals ensure that a UserProfile is automatically created
#  when a new user is registered.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Member', 'Member'),
        ('Librarian', 'Librarian'),
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()







