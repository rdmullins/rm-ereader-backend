from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books_api', views.BookViewSet)
router.register(r"author_books", views.Author_BookViewSet)
#router.register(r"booksearch", views.BookSearch)

urlpatterns = [
    path('', views.books),
    path('', include(router.urls)),
    path('booksearch/', views.BookSearch.as_view(), name="BookSearch"),
    path('authorsearch/', views.AuthorSearch.as_view(), name="AuthorSearch"),
    path('subjectsearch/', views.SubjectSearch.as_view(), name="SubjectSearch"),
    path("author_book/<str:pk>/", Author_BookAPIView.as_view(), name="AuthorBookLookup"),
    path("bookmetadata/<str:gut_id>/", BookMetaDataView.as_view(), name="MetaDataLookup"),
]
