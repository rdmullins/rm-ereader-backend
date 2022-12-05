from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters
from rest_framework.decorators import action
# Create your views here.

def books(request):
    return HttpResponse("This is the books endpoint.")

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post"]

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
    search_fields = ['book', 'author']

class Author_BookViewSet(ModelViewSet):
    queryset = Author_Book.objects.all()
    serializer_class = Author_BookSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter]
    search_fields = ['Book_title', 'Author_last_name', 'Subject_subject']

    @action(detail=True, methods=["GET"])
    def getBooksByAuthor(self, request, **kwargs):
        id = self.kwargs.get("pk")
        books = Book.objects.filter(author__id=id)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class Book_DetailViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book_DetailSerializer
    http_method_names = ["get", "post"]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "last_name", "subject"]


# class ArtistViewSet(ModelViewSet):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

#     # returns songs from artist
#     @action(detail=True, methods=['GET'])
#     def getSongsByArtist(self, request, **kwargs):
#         id = self.kwargs.get('pk')
#         songs = Song.objects.filter(artist__id=id)
#         serializer = SongSerializer(songs, many=True)
#         return Response(serializer.data)

class BookSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class AuthorSearch(generics.ListAPIView):
    queryset = Author_Book.objects.all()
    serializer_class = Author_BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name']

# class AuthorSearch(generics.ListAPIView):
#     serializer_class_Author = AuthorSerializer
#     serializer_class_Book = BookSerializer

#     def get(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             query1 = Author.objects.all()
#             query2 = Book.objects.all()

#             serializer1 = self.serializer_class_Author(query1)
#             serializer2 = self.serializer_class_Book(query2)

#             filter_backends = [filters.SearchFilter]
#             search_fields = [Author.last_name]

#             return Response(
#                 {
#                     'author':serializer1.data,
#                     'book': serializer2.data,
#                 }
#             )

class SubjectSearch(generics.ListAPIView):
    queryset = Subject_Book.objects.all()
    serializer_class = Subject_BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject']

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

# def testing(request):
#     collections = Collection_Book.objects.all().values()
#     context = {
#         "Collections": collections,
#     }
#     return HttpResponse(collections)