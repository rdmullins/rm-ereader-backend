from django.contrib import admin
from .models import CustomUser
from .models import Author
from .models import Author_Role
from .models import Subject
from .models import Gutenberg_Type
from .models import Book
from .models import Book_Status
from .models import User_Book
from .models import Collection
from .models import User_Collection
from .models import Author_Book
from .models import Subject_Book
from .models import Collection_Book
from .models import BookMetaData
from .models import Narrator
from .models import AudioTracks
from .models import AudioBook



# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Author_Role)
admin.site.register(Subject)
admin.site.register(Gutenberg_Type)
admin.site.register(Book)
admin.site.register(Book_Status)
admin.site.register(User_Book)
admin.site.register(Collection)
admin.site.register(User_Collection)
admin.site.register(Author_Book)
admin.site.register(Subject_Book)
admin.site.register(Collection_Book)
admin.site.register(BookMetaData)
admin.site.register(Narrator)
admin.site.register(AudioTracks)
admin.site.register(AudioBook)


# search_fields = [Author.last_name, Subject.subject, Book.title, Author_Book.book]