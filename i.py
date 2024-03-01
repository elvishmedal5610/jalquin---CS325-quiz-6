#This programs satisfies the I in SOLID because it takes the interfaces and segregates them into smaller ones
from abc import ABC, abstractmethod

class BookCatalog(ABC):
    @abstractmethod
    def search_by_title(self, title):
        raise NotImplementedError("Subclasses must implement search_by_title method")

    @abstractmethod
    def search_by_author(self, author):
        raise NotImplementedError("Subclasses must implement search_by_author method")

    @abstractmethod
    def search_by_genre(self, genre):
        raise NotImplementedError("Subclasses must implement search_by_genre method")

class BookManager(ABC):
    @abstractmethod
    def add_book(self, book):
        raise NotImplementedError("Subclasses must implement add_book method")

    @abstractmethod
    def remove_book(self, book):
        raise NotImplementedError("Subclasses must implement remove_book method")

class BookLending(ABC):
    @abstractmethod
    def borrow_book(self, user, book):
        raise NotImplementedError("Subclasses must implement borrow_book method")

    @abstractmethod
    def return_book(self, user, book):
        raise NotImplementedError("Subclasses must implement return_book method")

class ReportGenerator(ABC):
    @abstractmethod
    def generate_borrowing_report(self):
        raise NotImplementedError("Subclasses must implement generate_borrowing_report method")

    @abstractmethod
    def generate_overdue_report(self):
        raise NotImplementedError("Subclasses must implement generate_overdue_report method")

    @abstractmethod
    def generate_popularity_report(self):
        raise NotImplementedError("Subclasses must implement generate_popularity_report method")

class GuestUser(BookCatalog):
    def search_by_title(self, title):
        print("Guest user searching book by title:", title)

    def search_by_author(self, author):
        print("Guest user searching book by author:", author)

    def search_by_genre(self, genre):
        print("Guest user searching book by genre:", genre)

class Librarian(BookCatalog, BookManager, BookLending, ReportGenerator):
    def search_by_title(self, title):
        print("Librarian searching book by title:", title)

    def search_by_author(self, author):
        print("Librarian searching book by author:", author)

    def search_by_genre(self, genre):
        print("Librarian searching book by genre:", genre)

    def add_book(self, book):
        print("Librarian adding book to catalog:", book)

    def remove_book(self, book):
        print("Librarian removing book from catalog:", book)

    def borrow_book(self, user, book):
        print("Librarian lending book to user:", user, book)

    def return_book(self, user, book):
        print("Librarian returning book from user:", user, book)

    def generate_borrowing_report(self):
        print("Librarian generating borrowing report")

    def generate_overdue_report(self):
        print("Librarian generating overdue report")

    def generate_popularity_report(self):
        print("Librarian generating popularity report")

def main():
    guest_user = GuestUser()
    guest_user.search_by_title("Python Programming")

    librarian = Librarian()
    librarian.add_book("Python Programming")
    librarian.generate_borrowing_report()

if __name__ == "__main__":
    main()
