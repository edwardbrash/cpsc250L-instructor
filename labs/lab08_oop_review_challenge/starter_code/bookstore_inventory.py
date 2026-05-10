# Lab 8: Object-Oriented Programming Review Challenge

from book import Book

def create_inventory():
    """
    Create and return a list of Book objects.
    """
    books = []

    import csv
    f = open("../data/booklist.csv", "r")
    reader = csv.reader(f)
    for row in reader:
        books.append(Book(row[0], row[1], row[2], row[3], row[4], row[5]))

    return books


def print_inventory(books):
    """
    Print every book in the inventory.
    """
    for book in books:
        print(book)


def total_inventory(books):
    """
    Return the total number of all books in inventory.
    """
    total_books = 0
    for book in books:
        total_books += 1

    return total_books

def find_by_author(books, author):
    """
    Return a list of books written by the specified author.
    """
    book_list = []
    for book in books:
        if book.author == author:
            book_list.append(book)
    return book_list


def find_low_stock(books, threshold):
    """
    Return a list of books whose quantity is less than or equal to threshold.
    """
    book_list = []
    for book in books:
        if book.quantity < threshold:
            book_list.append(book)
    return book_list


def print_books(books):
    """
    Print a list of books.
    """
    for book in books:
        print(book)


def main():
    inventory = create_inventory()

    print("Full Inventory")
    print("--------------")
    print_inventory(inventory)

    print()
    print("Total inventory:", total_inventory(inventory))

    print()
    print("Books by Octavia Butler")
    print("-----------------------")
    print_books(find_by_author(inventory, "Octavia Butler"))

    print()
    print("Low Stock Books")
    print("---------------")
    print_books(find_low_stock(inventory, 1))

    print()
    print("Sorted by Title")
    print("---------------")
    sorted_books = sorted(inventory)
    print_books(sorted_books)


main()
