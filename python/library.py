from models.book import Book
from models.member import Member


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self):
        book_id = int(input("Book ID : "))
        title = input("Title : ")
        author = input("Author : ")

        self.books.append(Book(book_id, title, author))

        print("\nBook Added Successfully!")

    def add_member(self):
        member_id = int(input("Member ID : "))
        name = input("Member Name : ")

        self.members.append(Member(member_id, name))

        print("\nMember Added Successfully!")

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
            print("\nNo Books Available")
            return

        print("\nBook ID Title                     Author                    Status")
        print("-"*65)

        for book in self.books:
            print(book)

    def display_members(self):
        if not self.members:
            print("\nNo Members")
            return

        for member in self.members:
            member.display()

    def issue_book(self):

        member_id = int(input("Member ID : "))
        book_id = int(input("Book ID : "))

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            print("Member Not Found")
            return

        if book is None:
            print("Book Not Found")
            return

        if not book.available:
            print("Book Already Issued")
            return

        member.issued_books.append(book.title)
        book.available = False

        print("Book Issued Successfully")

    def return_book(self):

        member_id = int(input("Member ID : "))
        book_id = int(input("Book ID : "))

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None or book is None:
            print("Invalid Details")
            return

        if book.title not in member.issued_books:
            print("Book not issued by this member")
            return

        member.issued_books.remove(book.title)

        book.available = True

        print("Book Returned Successfully")