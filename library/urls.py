from django.urls import path

from library.views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, \
    AuthorCreateView, AuthorUpdateView, AuthorListView

app_name = 'library'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),

    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),


]



