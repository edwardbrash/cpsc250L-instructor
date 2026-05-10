# Lab 8: OOP Review Challenge


class Book:
    def __init__(self, title, author, year, genre, pages, rating):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.rating = rating
        self.quantity = 1

    def add_stock(self, amount):
        """
        Increase quantity by amount.
        """
        self.quantity += amount

    def sell_copies(self, amount):
        """
        Decrease quantity by amount if enough copies are available.

        Return True if the sale succeeds.
        Return False otherwise.
        """
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        else:
            return False

    def __str__(self):
        """
        Return a string representation of the book.
        """
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}, Rating: {self.rating}"

    def __lt__(self, other):
        """
        Compare books alphabetically by title.
        """
        return self.title < other.title
