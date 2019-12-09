from BookStoreOODClass import *
# imports everything from the file


def main():
    cashbalance = 1000
    CountryClubBookstore = BookStore(cashbalance)
    # can also do BookStore(1000) since you're essentially hard coding it

    while True:
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
        # TODO
        # do this for each case

        if mainmenu.upper() == "A":
            title = input("What is the title of the book you are adding: ")
            author = input("What is the authors name: ")
            cost = input("What is the price of this book: ")
            CountryClubBookstore.add_book(title, author, cost)

        elif mainmenu.upper() == "A":
            None

        elif mainmenu.upper() == "S":
            None

        elif mainmenu.upper() == "R":
            None

        elif mainmenu.upper() == "I":
            None

        elif mainmenu.upper() == "V":
            None

        elif mainmenu.upper() == "P":
            None

        elif mainmenu.upper() == "O":
            None

        elif mainmenu.upper() == "Q":
            print("Goodbye...")
            break

        else:
            print("Oops you must've entered an incorrect command")




if __name__ == "__main__":
    main()
