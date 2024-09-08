# API Views
This project uses Django REST Framework's generic views to handle CRUD operations for the Book model.
Views Overview

# BookListView:

Endpoint: /api/books/
Methods: GET, POST
Description: Lists all books and allows creation of new books.
Permissions: Read-only for unauthenticated users, full access for authenticated users.


# BookDetailView:

Endpoint: /api/books/<int:pk>/
Methods: GET, PUT, PATCH, DELETE
Description: Retrieves, updates, or deletes a specific book.
Permissions: Read-only for unauthenticated users, full access for authenticated users who are the author of the book.


# BookCreateView:

Endpoint: /api/books/create/
Methods: POST
Description: Creates a new book.
Permissions: Only authenticated users can create books.



# Custom Behavior

BookDetailView uses a custom permission IsAuthorOrReadOnly to ensure only the author of a book can edit or delete it.
BookCreateView automatically sets the authenticated user as the author of the newly created book.

# Permissions

Unauthenticated users have read-only access to book listings and details.
Authenticated users can create new books and edit/delete their own books.
The IsAuthorOrReadOnly permission ensures that only the author of a book can modify or delete it.

To use these views, ensure you're properly authenticated and have the necessary permissions.