class Book:
    # Class variable to track total number of books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment the book count when a new book is created
        Book.increment_book_count()

    # Class method to increment book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create book instances
book1 = Book("Python Basics")
book2 = Book("Advanced Python")
book3 = Book("Data Science with Python")

# Print the total number of books
print("Total books created:", Book.total_books)
