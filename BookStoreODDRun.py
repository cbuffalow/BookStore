from BookStoreOODClass import *


def main():
    run = True
    cashBalance = 1000
    CountryClubBookStore = BookStore(1000)

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
            if titleAdd.isalpha():
                if authorAdd.isalpha():
                    if costAdd.isdigit():
                        if int(costAdd) > 0:  # cost cant be non zero
                            if cashBalance - int(costAdd) >= 0:  # have enough cash
                                cashBalance -= (int(costAdd) * .90)  # reduce cash

                                if authorAdd != "":
                                    if titleAdd != "":  # add author and title to appropriate lines
                                        costAdd = int(costAdd)
                                        CountryClubBookStore.addbook(titleAdd, authorAdd, costAdd)
                                    else:
                                        print("The title was blank")

                                else:
                                    print("Author was blank")
                            else:
                                print("Insufficient funds.")
                        else:
                            print("Cost was zero which is invalid")
                    else:
                        print("Invalid Cost")
                else:
                    print("Invalid author")
            else:
                print("Invalid Title")

        elif mainmenu.upper() == "S":
                bookToSell = input("What book would you like to sell (just press enter to return to main menu): ")
                if bookToSell.isalpha():
                    CountryClubBookStore.sellbook(bookToSell)

                else:
                    print("Invalid Title.")

        elif mainmenu.upper() == "R":
            CountryClubBookStore.reduceprice()

        elif mainmenu.upper() == "I":
            CountryClubBookStore.increaseprice()

        elif mainmenu.upper() == "V":
            CountryClubBookStore.inventory()

        elif mainmenu.upper() == "P":
            CountryClubBookStore.saveinv()

        elif mainmenu.upper() == "O":
            CountryClubBookStore.openinv()

        elif mainmenu.upper() == "Q":
            print("Exiting...")
            run = False


if __name__ == "__main__":
    main()

