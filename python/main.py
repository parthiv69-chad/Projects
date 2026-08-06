from services.library import Library
from utils.menu import show_menu

library = Library("Central Library")

while True:

    show_menu()

    try:

        choice = int(input("\nEnter Choice : "))

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
            print("\nThank You!")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Enter Numbers Only")