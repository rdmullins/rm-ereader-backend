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
    gut_type = models.ForeignKey(Gutenberg_Type, on_delete=models.PROTECT)

class Book_Status(models.Model):
    status = models.CharField(max_length=255)