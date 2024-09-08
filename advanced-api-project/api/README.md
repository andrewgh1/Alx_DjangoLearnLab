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

# API Features
Filtering, Searching, and Ordering
The Book API now supports advanced querying capabilities including filtering, searching, and ordering.
Filtering
You can filter books based on the following fields:

title
author__name
publication_year

Example: /api/books/?publication_year=2023
Searching
The search functionality allows you to search across the following fields:

title
author__name

Example: /api/books/?search=Django
Ordering
You can order the results by the following fields:

title
publication_year
author__name

Use the minus sign (-) for descending order.
Example: /api/books/?ordering=-publication_year
Combining Features
You can combine filtering, searching, and ordering in a single query.
Example: /api/books/?publication_year=2023&search=Python&ordering=-title
Usage
To use these features, append the appropriate query parameters to your API requests. Multiple parameters can be combined using the & symbol.
Examples

Get all books published in 2023:
/api/books/?publication_year=2023
Search for books with "Python" in the title or author name, published in 2023, ordered by title (descending):
/api/books/?publication_year=2023&search=Python&ordering=-title
Get books by a specific author, ordered by publication year:
/api/books/?author__name=John%20Doe&ordering=publication_year

Testing
Running Tests
To run the test suite for the Book API, use the following command:
bashCopypython manage.py test api
This command will discover and run all the tests in the api application.
Test Cases
The test suite includes the following test cases:

test_list_books: Verifies that the API can list all books.
test_create_book: Ensures that authenticated users can create new books.
test_retrieve_book: Checks that individual books can be retrieved.
test_update_book: Verifies that authenticated users can update books.
test_delete_book: Ensures that authenticated users can delete books.
test_filter_books: Tests the filtering functionality of the book list.
test_search_books: Verifies the search functionality works correctly.
test_order_books: Checks that the ordering of books works as expected.
test_unauthenticated_create: Ensures unauthenticated users cannot create books.
test_unauthorized_update: Verifies that users cannot update books they don't own.

Interpreting Test Results
When you run the tests, Django will output the results of each test case. Here's how to interpret the output:

A dot (.) indicates a passed test.
An 'E' indicates an error occurred during the test.
An 'F' indicates a test failure.

At the end of the test run, you'll see a summary of how many tests were run and how many passed/failed.
If all tests pass, you'll see something like:
Copy----------------------------------------------------------------------
Ran 10 tests in 0.123s

OK
If any tests fail, you'll see details about which tests failed and why.
Troubleshooting
If you encounter test failures:

Read the error message carefully to understand which test failed and why.
Check the test case in test_views.py to see what was being tested.
Review your view logic and serializers to ensure they match the expected behavior.
Make necessary adjustments to your code or tests as needed.

Remember, failing tests don't necessarily mean your code is broken – they might also indicate that your tests need updating if you've intentionally changed the API's behavior.