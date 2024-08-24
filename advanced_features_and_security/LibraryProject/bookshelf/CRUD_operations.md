# -- CREATE --
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book}")
# Expected output: Book created: 1984

# -- RETRIEVE --
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
# Expected output: Title: 1984, Author: George Orwell, Year: 1949


# -- UPDATE --
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(f"Updated title: {updated_book.title}")
# Expected output: Updated title: Nineteen Eighty-Four


# -- DELETE --
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted")
print("All books:", Book.objects.all())
# Expected output:
# Book deleted
# All books: <QuerySet []>


