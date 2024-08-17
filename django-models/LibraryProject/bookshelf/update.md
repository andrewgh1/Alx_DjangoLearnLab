book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(f"Updated title: {updated_book.title}")
# Expected output: Updated title: Nineteen Eighty-Four
