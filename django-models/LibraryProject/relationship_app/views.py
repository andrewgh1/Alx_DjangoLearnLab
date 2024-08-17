from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the relationship_app index.")

#fbv
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

#cbv
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
