from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"books_api", BookViewSet, basename="Book")

urlpatterns = [
    path('', views.books, name='books'),
]