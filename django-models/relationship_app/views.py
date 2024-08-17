from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView #cbv
from .models import Book #fbv
from .models import Library #cbv
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required #setup user login and logout authentication views


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
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

#LogoutView
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

#RegisterationView
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
#Authentication
@login_required
def profile_view(request):
    return render(request, 'relationship_app/profile.html')
