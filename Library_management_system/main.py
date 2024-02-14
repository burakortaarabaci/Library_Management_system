from library import Library

lib = Library()

print("""

📚-WELCOME THE LIBRARY MANAGEMENT SYSTEM-📚

*** MENU ***

1) List Books
2) Add Book
3) Remove Book

If you want to quit press, 'Q'.

""")
is_on = True
while is_on:
    user_choice = input("Enter your choice (1-3 or 'Q'):").lower()
    if user_choice == "1":
        lib.list_books()
    elif user_choice == "2":
        lib.add_book()
    elif user_choice == "3":
        lib.remove_book()
    elif user_choice == "q":
        print("Quiting.. GoodBye..Thanks Global AI Hub and AKBANK")
        is_on = False
    else:
        print("Invalid input! Please enter one of the options above. ")