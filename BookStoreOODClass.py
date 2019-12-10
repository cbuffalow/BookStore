class BookStore:

    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = ""
        self.bookstore = []
        self.bookstore = self.title, self.author, self.cost = [], [], []
        self.books = []
        self.cash = 1000

    def update_cost(self, new_cost):
        self.cost = new_cost

    def addbook(self, title, author, cost):
        self.title.append(title)
        self.author.append(author)
        self.cost.append(cost)
        print(self.bookstore)

    def sellbook(self, Book):
        for i in self.bookstore:
            i.remove(Book)

    def inventory(self):
        print(self.bookstore)







