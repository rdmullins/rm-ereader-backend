from django.urls import path, include
from . import views
# from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books_api', views.BookViewSet)
router.register(r"author_books", views.Author_BookViewSet)
#router.register(r"booksearch", views.BookSearch)

urlpatterns = [
    path('', views.books),
    path('', include(router.urls)),
    path('booksearch/', views.BookSearch.as_view(), name="BookSearch"),
]
