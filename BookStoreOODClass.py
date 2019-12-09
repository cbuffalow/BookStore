class Book:
    """Book is an object with a title, author, and a price"""
    def __init__(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def update_cost(self, new_cost):
        self.cost = new_cost


class BookStore:
    """Bookstore is the main object that is created once and updated when necessary
    i.e: buying / selling books, changing prices"""
    books = []  # empty list
    cash = 0    # starts at zero before init method is called

    def __init__(self, seed_money):
        self.cash = seed_money

    def add_book(self, title, author, cost):
        self.books.append(Book(title, author, cost))

    def sell_book(self, book):  # takes in a book object to remove
        cost = book.cost
        self.books.remove(book)
        # .remove only removes an object so it searches for the Book that matches
        self.cash += cost  # increase cash because the book was sold

    def increase_prices(self):
        for i in range(len(self.books)):
            temp = self.books.pop(i)  # remove at index
            temp.update_cost(1.1*temp.cost)  # increase price of books by 10%
            self.books.insert(i, temp)  # insert back at correct index

    def decrease_prices(self):
        for i in range(len(self.books)):
            temp = self.books.pop(i)  # remove at index
            temp.update_cost(.9*temp.cost)  # decrease price of books by 10%
            self.books.insert(i, temp)  # insert back at correct index
