from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')
