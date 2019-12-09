def main():
        import pickle
        run = True
        cashBalance = 1000
        bookstore = titles, authors, prices = [], [], []

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
            if mainmenu.upper() == "A":  # add book
                title = input("What is the title of the book you are adding: ")
                author = input("What is the book's author: ")
                cost = input("What is the cost of the book: ")
                if title.isalpha():
                    if author.isalpha():
                        if cost.isdigit():
                            if int(cost) > 0:  # cost cant be non zero
                                if cashBalance - int(cost) >= 0:  # have enough cash
                                    cashBalance -= (int(cost) * .90)  # reduce cash

                                    if author != "":
                                        if title != "":  # add author and title to appropriate lines
                                            titles.append(title)
                                            authors.append(author)
                                            prices.append((int(cost) * .90))
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
            elif mainmenu.upper() == "S":  # sell book (increases cash bal) deletes book from inv
                bookToSell = input("What book would you like to sell (just press enter to return to main menu): ")

                if bookToSell != "\n":  # enter was not pressed
                    okayToSell = False  # initialized boolean to fasle until all checks passed
                    index = None
                    for i in range(len(titles)):
                        if titles[i] == bookToSell:
                            index = i
                            okayToSell = True
                            break
                        else:
                            print("Book does not exist.")
                    if okayToSell:
                        # remove book from database
                        del authors[index]
                        del titles[index]
                        priceToAdd = prices.pop(index)  # pop gives item and removes it at the same time
                        cashBalance = cashBalance + int(priceToAdd)  # add cash from selling book
                        print("Sale successful!")
                    else:
                        print("Exiting to main menu...")

            elif mainmenu.upper() == "R":  # reduce cost by 2%
                for i in range(len(prices)):
                    prices[i] *= .98

            elif mainmenu.upper() == "I":  # increase cost by 2%
                for i in range(len(prices)):
                    prices[i] *= 1.02

            elif mainmenu.upper() == "V":  # displays inventory
                """
                Title:
                Author:
                Our Cost (current cost):
    
                Anticipated selling price (current cost X 1.1):
                Anticipated profit (selling price X .10):
                ...
                Cash Balance: 
                """
                for i in range(len(prices)):
                    tempTitle = titles[i]
                    tempAuthor = authors[i]
                    tempPrice = prices[i]
                    sellingPrice = tempPrice * 1.1
                    profit = sellingPrice * .1
                    print(tempTitle + " by " + tempAuthor + " at cost of us: $ " + str(format(tempPrice, '.2f')))
                    print("Anticipated selling price: " + str(format(sellingPrice, '.2f')))
                    print("Anticipated profit/revenue: " + str(format(profit, '.2f')))

                print("Current cash balance: " + str(cashBalance))

            elif mainmenu.upper() == "P":  #pickles list and clears current inv

                savename = input("What would you like to call the file you will save the inventory too: ")
                pickle_out = open(savename, "wb")
                titles_obj = titles
                authors_obj = authors
                prices_obj = prices
                pickle.dump(titles_obj, pickle_out)
                pickle.dump(authors_obj, pickle_out)
                pickle.dump(prices_obj, pickle_out)
                pickle_out.close()
                del titles[:]
                del authors[:]
                del prices[:]
                print(bookstore)
            elif mainmenu.upper() == "O":

                readfile = input("What is the file name you of the inventory you would like to open: ")
                pickle_in = open(readfile, "rb")
                titles_obj = pickle.load(pickle_in)
                authors_obj = pickle.load(pickle_in)
                prices_obj = pickle.load(pickle_in)
                titles = titles_obj
                authors = authors_obj
                prices = prices_obj

            elif mainmenu.upper() == "Q":
                print("Exiting...")
                run = False


if __name__ == '__main__':
    main()

