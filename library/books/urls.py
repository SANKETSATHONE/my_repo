from django.urls import path
from books.views import get_all_books, get_single_book


urlpatterns = [
    path("home/", get_all_books),
    path('get/<int:id>',get_single_book)
]