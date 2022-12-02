from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """ 
    only pull in the PROVIDED DJANGO USER FIELDS that are going to be used in creating a user, 
    and then add your extended fields,
    '__all__' pulls in all fields and creates an error for the validation step below
    """
    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

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
        return '%s (%s, %s)\n\tGutenberg ID: %s\n\tLibrivox ID: %s' %(self.title, self.gut_issued, self.gut_type, self.gut_id, self.lib_id)

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
    author = models.ManyToManyField(Author, related_name="author_of_book")
    book = models.ManyToManyField(Book, related_name="book_info")
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

class BookMetaData(models.Model):
    fulltext = models.TextField()
    epub = models.FileField(null=True)
    cover = models.FileField(null=True)
    gut_id = models.IntegerField(null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return self.book.title