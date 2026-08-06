from models.person import Person

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
                print("-", book)
        else:
            print("Issued Books : None")