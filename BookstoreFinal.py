def main():
    run = True
    bookstore = dict()
    cashBalance = 1000
    bookprices= dict()
    while run:
        mainmenu = raw_input('''What would you like to do?
                                A. Add Book
                                S. Sell Book
                                R. Reduce book prices across the board by 2%
                                I. Increase book prices across the board by 2%
                                V. Display inventory
                                Q. Quit
                                        :  ''')
        if mainmenu.upper() == "A":
                    #add book
            titleAdd = raw_input("What is the title of the book you are adding: ")
            authorAdd = raw_input("What is the book's author: ")
            costAdd = raw_input("What is the cost of the book: ")

            if cashBalance - int(costAdd) <= 0:
                print("Insufficient Funds.")
                costAdd = 0

            elif costAdd.isdigit():
                bookstore[titleAdd] = authorAdd, costAdd
                bookprices[titleAdd] = costAdd
                cashBalance = cashBalance - (int(costAdd)*.90)
                print cashBalance
                print bookstore

            else:
                print("Invalid Cost")

        elif mainmenu.upper() == "S":

                #sell book
            bookSell = raw_input("What book would you like to sell (just press enter to return to main menu): ")

            if not bookSell:
                print("Exiting to main menu...")
                break
                #remove book from database
            if bookSell in bookstore:
                del bookstore[bookSell]
                del bookprices[bookSell]
                #add cash to balance from sale
                cashBalance = cashBalance + int(costAdd)

                print("Sale successful!")
            else:
                print("Book does not exist.")
            print cashBalance
            print bookstore

        elif mainmenu.upper() == "R":
                #reduce cost by 2%
            for titleAdd in bookprices.keys():
                costAdd = bookprices[titleAdd]
                newprice =  int(costAdd) * .98
                costAdd = newprice
                bookstore[titleAdd] = authorAdd, costAdd
                bookprices[titleAdd] = costAdd

        elif mainmenu.upper() == "I":
                #increase cost by 2%
            for titleAdd in bookprices.keys():
                costAdd = bookprices[titleAdd]
                newprice =  int(costAdd) * 1.02
                costAdd = newprice
                bookstore[titleAdd] = authorAdd, costAdd
                bookprices[titleAdd] = costAdd

        elif mainmenu.upper() == "V":
                #displays inventory
                for costAdd in bookprices.keys():
                    costAdd = bookprices[titleAdd]
                    salesprice = int(costAdd) * 1.10
                print("Book title, Author, and Cost: ", bookstore)
                print("Estimated Price book will sell for: ", salesprice)
                print("Current Cash Balance: ", cashBalance)

        elif mainmenu.upper() == "Q":
                #quit
            print("Exiting...")
            run = False

if __name__ == '__main__':
    main()

