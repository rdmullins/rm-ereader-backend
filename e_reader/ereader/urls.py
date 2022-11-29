from django.urls import path, include
from . import views
# from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books_api', views.BookViewSet)

urlpatterns = [
    path('', views.books),
    path('', include(router.urls)),
]
