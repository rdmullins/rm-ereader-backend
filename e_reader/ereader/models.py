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
    dob = models.CharField(max_length=4)
    dod = models.CharField(max_length=4)

    def __str__(self):
        return '%s, %s (%s - %s)' % (self.last_name, self.first_name, self.dob, self.dod)

class Author_Role(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

class Subject(models.Model):
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject

class Gutenberg_Type(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

class Book(models.Model):
    title = models.CharField(max_length=255)
    gut_id = models.IntegerField()
    lib_id = models.IntegerField(blank=True)
    gut_issued = models.DateField(blank=True)
    description = models.TextField(default="No Description Available")
    gut_type = models.ForeignKey(Gutenberg_Type, on_delete=models.PROTECT)

    def __str__(self):
        return '%s (%s, %s)\n\tGutenberg ID: %s\n\tLibrivox ID: %s\nDescription:\n\%s' %(self.title, self.gut_issued, self.gut_type, self.gut_id, self.lib_id, self.description)

class Book_Status(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        self.status

class User_Book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    book_status = models.ForeignKey(Book_Status, on_delete=models.PROTECT)
    farthest_read = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return 'User: %s\nBook: %s' % (self.user, self.book)

class Collection(models.Model):
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User_Collection(models.Model):
    collection = models.ManyToManyField(Collection)
    user = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.collection

class Author_Book(models.Model):
    author = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    author_role = models.ForeignKey(Author_Role, on_delete=models.PROTECT)

    def __str__(self):
        return ('%s, %s (%s)') % (self.author, self.book, self.author_role)

class Subject_Book(models.Model):
    subject = models.ManyToManyField(Subject)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return ('%s, %s') % (self.subject, self.book)

class Collection_Book(models.Model):
    collection = models.ManyToManyField(Collection)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return ('%s, %s') % (self.collection, self.book)