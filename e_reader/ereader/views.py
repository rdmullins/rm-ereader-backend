from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters

# Create your views here.

def books(request):
    return HttpResponse("This is the books endpoint.")

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post"]

class Author_BookViewSet(ModelViewSet):
    queryset = Author_Book.objects.all()
    serializer_class = Author_BookSerializer
    http_method_names = ["get", "post"]

class BookSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']