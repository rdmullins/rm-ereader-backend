from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def books(request):
    return HttpResponse("This is the books endpoint.")

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post"]