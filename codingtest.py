class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Sorry, this book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("This book was not borrowed.")

    def __str__(self):
        if self.available:
            status = "Available"
        else:
            status = "Borrowed"
        return self.title + " by " + self.author + " - " + status


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Diary of a Wimpy Kid", "Jeff Kinney")

print(book1)
print(book2)
print(book3)

print("\nBorrowing Harry Potter:")
book1.borrow()
print(book1)

print("\nBorrowing Harry Potter again:")
book1.borrow()

print("\nReturning Harry Potter:")
book1.return_book()
print(book1)

print("\nBorrowing The Hobbit:")
book2.borrow()
print(book2)

print("\nReturning The Hobbit:")
book2.return_book()
print(book2)