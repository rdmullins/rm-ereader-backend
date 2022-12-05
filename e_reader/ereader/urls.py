from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books_api', views.BookViewSet)
router.register(r"author_books", views.Author_BookViewSet)
router.register(r"author_book_detail", views.Author_Book_DetailViewSet)
router.register(r"book_detail", views.Book_DetailViewSet)
router.register(r"collection_API", views.Collection_API_ReturnViewSet)
router.register(r"subject_book_API", views.Subject_API_ReturnViewSet)
#router.register(r"booksearch", views.BookSearch)

urlpatterns = [
    path('', views.books),
    path('', include(router.urls)),
    path('booksearch/', views.BookSearch.as_view(), name="BookSearch"),
    path('authorsearch/', views.AuthorSearch.as_view(), name="AuthorSearch"),
    path('subjectsearch/', views.SubjectSearch.as_view(), name="SubjectSearch"),
    path('collectionsearch/', views.CollectionSearch.as_view(), name="CollectionSearch"),
    path('bookbyid/', views.BookById.as_view(), name="BookByID"),
    path("author_book/<str:pk>/", Author_BookAPIView.as_view(), name="AuthorBookLookup"),
    path("collection_book/<str:pk>/", Collection_BookAPIView.as_view(), name="CollectionBookLookup"),
    path("bookmetadata/<str:gut_id>/", BookMetaDataView.as_view(), name="MetaData"),
    path("bookmetadatalookup/<str:gut_id>/", BookMetaDataLookupAPIView.as_view(), name="MetaDataLookup"),
    #path("collection_api/", Collection_API_ReturnViewSet.as_view(), name="CollectionAPI"),
    #path("testing/", views.testAPI.as_view(), name="Testing"),
    #path("author_book_detail", Author_Book_DetailViewSet.as_view(), name="AuthorBookDetail"),
]
