from BookStoreOODClass import Book

cashbalance = 1000
run = True

while run:
    mainmenu = input('''What would you like to do?
                                    A. Add Book
                                    S. Sell Book
                                    R. Reduce book prices across the board by 2%
                                    I. Increase book prices across the board by 2%
                                    V. Display inventory
                                    P. Save current inventory
                                    O. Open and load an inventory
                                    Q. Quit
                                            :  ''')
    if mainmenu.upper() == "A":
        titleAdd = input("What is the title of the book you are adding: ")
        authorAdd = input("What is the authors name: ")
        costAdd = input("What is the price of this book: ")
        Book.addbook(titleAdd, authorAdd, costAdd)



