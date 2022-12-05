from rest_framework import serializers
from .models import *
from .fields import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class Author_RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_Role
        fields = "__all__"

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class Gutenberg_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gutenberg_Type
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "gut_id", "lib_id", "gut_issued", "description", "gut_type")
    gut_type = Gutenberg_TypeSerializer()

class Author_BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    book = BookSerializer(many=True)
    author_role = Author_RoleSerializer()
    # subject = SubjectSerializer(many=True)
    # author = serializers.SerializerMethodField()
    # book = serializers.SerializerMethodField()
    # author_role = serializers.SerializerMethodField()
    
    class Meta:
        model = Author_Book
        fields = "__all__"
        depth = 1

    # def get_author(self, obj):
    #     return obj.book.first().author.first_name

    # def get_book(self,obj):
    #     book = obj.book.all()
    #     author_book_view = []
    #     for volume in book:
    #         title = book.title
    #         author_of_book = author
    #         author_book_view.append(f'Book: {title}, Author: {author_of_book}')
    #     return author_book_view


class Subject_BookSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)
    book = BookSerializer(many=True)

    class Meta:
        model = Subject_Book
        fields = "__all__"

class Collection_BookSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(many=True)
    book = BookSerializer(many=True)
    depth = 4

    class Meta:
        model = Collection_Book
        fields = "__all__"

class Author_SearchSerializer(serializers.ModelSerializer):
    # author = AuthorListingField(many=True, read_only=True)

    class Meta:
        model = Author_Book
        fields = ('book_info',)

class BookMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMetaData
        fields = "__all__"

class Author_Book_Detail_SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_Book
        fields = "__all__"
        depth = 2

class Book_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 2