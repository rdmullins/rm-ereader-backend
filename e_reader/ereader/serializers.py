from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class Author_RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_Role
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
        fields = "__all__"
    gut_type = Gutenberg_TypeSerializer()

class Author_BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    book = BookSerializer(many=True)
    author_role = Author_RoleSerializer()

    class Meta:
        model = Author_Book
        fields = "__all__"

class Subject_BookSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)
    book = BookSerializer(many=True)

    class Meta:
        model = Subject_Book
        fields = "__all__"