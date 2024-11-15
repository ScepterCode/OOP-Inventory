class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():  # Borrow only if the book is available
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self):
        self.books = []  # Catalog of books
        self.members = {}  # Dictionary of members by member_id

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library catalog.")

    def register_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            print(f"Member '{member.name}' registered successfully.")
        else:
            print(f"Member '{member.name}' is already registered.")

    def lend_book(self, book, member):
        if member.member_id not in self.members:
            print(f"Error: {member.name} is not registered in the library.")
            return False
        if member.borrow_book(book):
            print(f"{member.name} successfully borrowed '{book.title}'.")
            return True
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")
            return False

    def receive_book(self, book, member):
        if member.return_book(book):
            print(f"{member.name} has returned '{book.title}'.")
            return True
        else:
            print(f"{member.name} does not have '{book.title}' to return.")
            return False

    def check_availability(self, title):
        for book in self.books:
            if book.title == title:
                return f"{title} is {'available' if book.is_available else 'unavailable'}."
        return f"{title} not found in the catalog."

    def show_all_books(self):
        if not self.books:
            print("No books in the library catalog.")
        else:
            print("Library Catalog:")
            for book in self.books:
                status = "Available" if book.is_available else "Unavailable"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    self.books.remove(book)
                    print(f"Book '{title}' removed from the library catalog.")
                    return True
                else:
                    print(f"Cannot remove '{title}' because it is currently borrowed.")
                    return False
        print(f"Book '{title}' not found in the library catalog.")
        return False


# Interactive command loop for sequential operations
library = Library()

def library_system():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Register a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Check Book Availability")
        print("6. Show All Books")
        print("7. Remove a Book")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.register_member(member)

        elif choice == "3":
            member_id = input("Enter member ID: ")
            title = input("Enter the title of the book to borrow: ")
            member = library.members.get(member_id)
            if not member:
                print(f"No member found with ID {member_id}.")
                continue
            book = next((b for b in library.books if b.title == title), None)
            if not book:
                print(f"Book '{title}' not found in the library catalog.")
                continue
            library.lend_book(book, member)

        elif choice == "4":
            member_id = input("Enter member ID: ")
            title = input("Enter the title of the book to return: ")
            member = library.members.get(member_id)
            if not member:
                print(f"No member found with ID {member_id}.")
                continue
            book = next((b for b in library.books if b.title == title), None)
            if not book:
                print(f"Book '{title}' not found in the library catalog.")
                continue
            library.receive_book(book, member)

        elif choice == "5":
            title = input("Enter the title of the book to check availability: ")
            print(library.check_availability(title))

        elif choice == "6":
            library.show_all_books()

        elif choice == "7":
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == "8":
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid option. Please choose again.")

# Run the interactive library system
library_system()
