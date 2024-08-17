from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example usage:
if __name__ == "__main__":
    # And thats me assuming i have already created some data
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    for book in query_books_by_author(author_name):
        print(book.title)

    print(f"\nBooks in {library_name}:")
    for book in list_books_in_library(library_name):
        print(book.title)

    librarian = get_librarian_for_library(library_name)
    print(f"\nLibrarian of {library_name}: {librarian.name}")