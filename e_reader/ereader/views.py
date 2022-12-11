from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters
from rest_framework.decorators import action
from drf_multiple_model.views import ObjectMultipleModelAPIView
# Create your views here.

def books(request):
    return HttpResponse("This is the books endpoint.")

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post"]

class AudioBookViewSet(ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['book__gut_id']

class Subject_API_ReturnViewSet(ModelViewSet):
    queryset = Subject_Book.objects.all()
    serializer_class = Subject_BookSerializer

class Collection_API_ReturnViewSet(ModelViewSet):
    queryset = Collection_Book.objects.all()
    serializer_class = Collection_BookSerializer

    # @action(detail=True, methods=["get"])
    # def getBooksByCollection(self, request, **kwargs):
    #     id = self.kwargs.get("pk")
    #     books = Book.objects.filter(collection__id=id)
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data)

class Author_Book_DetailViewSet(ModelViewSet):
    queryset = Author_Book.objects.all()
    serializer_class = Author_Book_Detail_SearchSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authors', 'subjects']

class Author_BookViewSet(ModelViewSet):
    queryset = Author_Book.objects.all()
    serializer_class = Author_BookSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'authors', 'subjects']

class Book_DetailViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book_DetailSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "authors", "subjects"]

class BookSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class AuthorSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['authors__last_name']

class SubjectSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subjects__subject']

class CollectionSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['collections__name']

class Collections(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

# class CollectionBooks(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = []

class BookById(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id"]

class BookMetaDataView(generics.ListAPIView):
    queryset = BookMetaData.objects.all()
    serializer_class = BookMetaDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['gut_id']

class BookMetaDataLookupAPIView(APIView):

# Read Functionality

    def get_object(self, gut_id):
        try:
            return BookMetaData.objects.get(gut_id=gut_id)
        except BookMetaData.DoesNotExist:
            raise Http404

    def get(self, request, gut_id=None, format=None):
        if gut_id:
            data = self.get_object(gut_id)
            serializer = BookMetaDataSerializer(data)
        else:
            data = BookMetaData.objects.all()
            serializer = BookMetaDataSerializer(data, many=True)

        return Response(serializer.data)


class Author_BookAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Author_Book.objects.get(pk=pk)
        except Author_Book.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = Author_BookSerializer(data)
        else:
            data = Author_Book.objects.all()
            serializer = Author_BookSerializer(data, many=True)

        return Response(serializer.data)

class Collection_BookAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Collection_Book.objects.get(pk=pk)
        except Collection_Book.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = Collection_BookSerializer(data)
        else:
            data = Collection_Book.objects.all()
            serializer = Collection_BookSerializer(data, many=True)

        return Response(serializer.data)

class AudioBookView(APIView):

# Read Functionality

    def get_object(self, gut_id):
        try:
            return AudioBook.objects.get(gut_id=book__gut_id)
        except AudioBook.DoesNotExist:
            raise Http404

    def get(self, request, gut_id=None, format=None):
        if gut_id:
            data = self.get_object(book__gut_id)
            serializer = AudioBookSerializer(data)
        else:
            data = AudioBook.objects.all()
            serializer = AudioBookSerializer(data, many=True)

        return Response(serializer.data)



