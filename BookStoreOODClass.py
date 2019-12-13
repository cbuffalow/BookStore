import pickle


class BookStore():

    def __init__(self, seed_money):
        self.title = ""
        self.author = ""
        self.cost = ""
        self.bookstore = self.title, self.author, self.cost = [], [], []
        self.cash = seed_money

    def update_cost(self, new_cost):
        self.cost = ""

    def addbook(self, title, author, cost): #adds new book
        self.title.append(title)
        self.author.append(author)
        self.cost.append(int(cost * .90))
        self.cash -= (int(cost) * .90)
        print(self.bookstore)
        print(self.cash)

    def sellbook(self, Book): #sells book
        okayToSell = False
        for i in range(len(self.title)):
            if self.title[i] == Book:
                index = i
                okayToSell = True
                break
            else:
                print("Searching for book...")
        if okayToSell:
            # remove book from database
            del self.author[index]
            del self.title[index]
            priceToAdd = self.cost.pop(index)  # pop gives item and removes it at the same time
            priceToAdd = (priceToAdd * 1.1)
            self.cash = self.cash + int(priceToAdd)  # add cash from selling book
            print("Sale successful!")
        else:
            print("Exiting to main menu...")

    def reduceprice(self): #decreases all book prices by 2%
        for i in range(len(self.cost)):
            self.cost[i] *= .98

    def increaseprice(self): #increases all book prices by 2%
        for i in range(len(self.cost)):
            self.cost[i] *= 1.02

    def inventory(self): #Displays inv
        """
                        Title:
                        Author:
                        Our Cost (current cost):

                        Anticipated selling price (current cost X 1.1):
                        Anticipated profit (selling price X .10):
                        ...
                        Cash Balance:
                        """
        for i in range(len(self.cost)):
            tempTitle = self.title[i]
            tempAuthor = self.author[i]
            tempPrice = self.cost[i]
            sellingPrice = tempPrice * 1.1
            profit = sellingPrice * .1
            print(tempTitle + " by " + tempAuthor + " at cost of us: $ " + str(format(tempPrice, '.2f')))
            print("Anticipated selling price: " + str(format(sellingPrice, '.2f')))
            print("Anticipated profit/revenue: " + str(format(profit, '.2f')))

        print("Current cash balance: " + str(format(self.cash, '.2f')))

    def saveinv(self): #pickles list and clears current inv
        savename = input("What would you like to call the file you will save the inventory too: ")
        pickle_out = open(savename, "wb")
        #establishes data to be recrded in file
        titles_obj = self.title
        authors_obj = self.author
        prices_obj = self.cost
        #dumps data to pickle file
        pickle.dump(titles_obj, pickle_out)
        pickle.dump(authors_obj, pickle_out)
        pickle.dump(prices_obj, pickle_out)
        pickle_out.close()
        #clears current inv
        del self.title[:]
        del self.author[:]
        del self.cost[:]
        print(self.bookstore)

    def openinv(self): #opens a saved inv and loads it into the current
        readfile = input("What is the file name you of the inventory you would like to open: ")
        pickle_in = open(readfile, "rb")
        titles_obj = pickle.load(pickle_in)
        authors_obj = pickle.load(pickle_in)
        prices_obj = pickle.load(pickle_in)
        self.title = titles_obj
        self.author = authors_obj
        self.cost = prices_obj






