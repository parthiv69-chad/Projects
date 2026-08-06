class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"

        return f"{self.book_id:<8}{self.title:<25}{self.author:<25}{status}"