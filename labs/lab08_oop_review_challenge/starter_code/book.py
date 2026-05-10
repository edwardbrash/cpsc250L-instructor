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
        # subtle point: let's ignore the first word of the title if it is "A" or "The"
        #
        #
        # Get first word of self.title and other.title
        self_first_word = self.title.split()[0]
        other_first_word = other.title.split()[0]
        # If first word is "A" or "The", strip it off for comparison
        if self_first_word == "A" or self_first_word == "The":
            self_title_comp = " ".join(self.title.split()[1:])
        else:
            self_title_comp = self.title

        if other_first_word == "A" or other_first_word == "The":
            other_title_comp = " ".join(self.title.split()[1:])
        else:
            other_title_comp = other.title

        # make comparison
        return self_title_comp < other_title_comp
