from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, member_id, name):
        self._member_id = member_id      
        self._name = name

    @abstractmethod
    def display(self):
        pass
class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.issued_books = []
    def display(self):
        print(f"\nMember ID : {self._member_id}")
        print(f"Name      : {self._name}")

        if self.issued_books:
            print("Issued Books:")
            for book in self.issued_books:
                print(" -", book)
        else:
            print("Issued Books : None")
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id:<8}{self.title:<25}{self.author:<25}{status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    def add_book(self):
        book_id = int(input("Enter Book ID : "))
        title = input("Enter Book Title : ")
        author = input("Enter Author Name : ")

        self.books.append(Book(book_id, title, author))
        print("\nBook added successfully!")

    def add_member(self):
        member_id = int(input("Enter Member ID : "))
        name = input("Enter Member Name : ")

        self.members.append(Member(member_id, name))
        print("\nMember added successfully!")
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    def find_member(self, member_id):
        for member in self.members:
            if member._member_id == member_id:
                return member
        return None

    def display_books(self):
        if not self.books:
            print("\nNo books available.")
            return

        print("\n---------------- BOOK LIST ----------------")
        print(f"{'Book ID':<8}{'Title':<25}{'Author':<25}Status")
        print("-" * 70)

        for book in self.books:
            print(book)

    def display_members(self):
        if not self.members:
            print("\nNo members found.")
            return

        print("\n--------------- MEMBER LIST ----------------")
        for member in self.members:
            member.display()
    def issue_book(self):
        member_id = int(input("Enter Member ID : "))
        book_id = int(input("Enter Book ID : "))

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print("\nMember not found!")
            return

        if book is None:
            print("\nBook not found!")
            return

        if not book.available:
            print("\nBook is already issued!")
            return

        member.issued_books.append(book.title)
        book.available = False

        print(f'\nBook "{book.title}" issued to {member._name}.')

    # Return Book
    def return_book(self):
        member_id = int(input("Enter Member ID : "))
        book_id = int(input("Enter Book ID : "))

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None or book is None:
            print("\nInvalid Member ID or Book ID!")
            return

        if book.title not in member.issued_books:
            print("\nThis member did not issue this book.")
            return

        member.issued_books.remove(book.title)
        book.available = True

        print(f'\nBook "{book.title}" returned successfully!')


# ------------------ Main Program ------------------
library = Library("Central Library")

while True:
    print("\n" + "=" * 50)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Display Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    try:
        choice = int(input("\nEnter your choice : "))

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.add_member()

        elif choice == 3:
            library.display_books()

        elif choice == 4:
            library.display_members()

        elif choice == 5:
            library.issue_book()

        elif choice == 6:
            library.return_book()

        elif choice == 7:
            print("\nThank you for using Library Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")

    except ValueError:
        print("\nPlease enter numbers only.")