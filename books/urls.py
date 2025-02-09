from django.urls import path
from .views import BookListCreate, BookDetailView

urlpatterns = [
    path("books/", BookListCreate.as_view()),
    path("book/<int:id>/", BookDetailView.as_view())
]