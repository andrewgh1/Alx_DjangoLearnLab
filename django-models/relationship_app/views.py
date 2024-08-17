from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView #cbv
from .models import Book #fbv
from .models import Library #cbv
from django.contrib.auth.views import LoginView ,LogoutView #setup user login and logout authentication views
from django.contrib.auth.forms import UserCreationForm #setup user login and logout authentication views
from django.urls import reverse_lazy #setup user login and logout authentication views
from django.views.generic.edit import CreateView #setup user login and logout authentication views


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

#setup user login and logout authentication views
#LoginView
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'


#LogoutView
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

#RegisterationView
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')