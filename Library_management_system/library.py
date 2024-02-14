class Library:
    def __init__(self):
        self.file = open("books.txt", "a+", encoding="UTF-8")

    def list_books(self):
        """This function shows the title and author of the books in the file."""
        self.file.seek(0)
        file_data = self.file.read()
        lines = file_data.splitlines()
        for book in lines:
            items = book.split(",")
            print(f"Book: {items[0]}  Author: {items[1]}")

    def add_book(self):
        """This function allows you to add a book to the file."""
        title = input("Enter the book title:").capitalize()
        author = input("Enter the author:").capitalize()
        year = input("Enter the release date:")
        number_of_pages = input("Enter the number of pages:")
        self.file.write(f"{title}, {author}, {year}, {number_of_pages}\n")
        print(f"'{title}' has been added successful..")

    def remove_book(self):
        """This function allows you to remove a book from the file."""
        book_title = input("Enter the book title to remove:").capitalize()
        self.file.seek(0)
        file_data = self.file.read()
        lines = file_data.splitlines()
        for book in lines:
            items = book.split(",")
            if items[0] == book_title:
                lines.remove(book)
        self.file.truncate(0)
        self.file.seek(0)
        for book in lines:
            self.file.write(f"{book}\n")
        print(f"'{book_title}' has been removed successful..")

    def __del__(self):
        self.file.close()



