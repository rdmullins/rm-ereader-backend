from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(blank=True)
    dod = models.DateField(blank=True)

class Author_Role(models.Model):
    role = models.CharField(max_length=255)

class Subject(models.Model):
    subject = models.CharField(max_length=255)

class Gutenberg_Type(models.Model):
    type = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    gut_id = models.IntegerField()
    lib_id = models.IntegerField()
    gut_issued = models.DateField(blank=True)
    description = models.TextField(default="No Description Available")
    gut_type = models.ForeignKey(Gutenberg_Type, on_delete=models.PROTECT)

class Book_Status(models.Model):
    status = models.CharField(max_length=255)

class User_Book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    book_status = models.ForeignKey(Book_Status, on_delete=models.PROTECT)
    farthest_read = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)

class User_Collection(models.Model):
    collection = models.ManyToManyField(Collection)
    user = models.ManyToManyField(CustomUser)

class Author_Book(models.Model):
    author = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    author_role = models.ForeignKey(Author_Role, on_delete=models.PROTECT)

class Subject_Book(models.Model):
    subject = models.ManyToManyField(Subject)
    book = models.ManyToManyField(Book)

class Collection_Book(models.Model):
    collection = models.ManyToManyField(Collection)
    book = models.ManyToManyField(Book)