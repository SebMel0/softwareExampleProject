class Library:

    def display(self):
        print("Books:")
        for book in self.__books:
            book.display()
            print("")
        print("Borrowers:")
        for borrower in self.__borrowers:
            borrower.display()
            print("")
        print("Loans:")
        for loan in self.__loans:
            loan.display()
            print("")
    
    def getBooks(self):
        return self.__books
    def getBorrowers(self):
        return self.__borrowers
    def getLoans(self):
        return self.__loans
    
   

    def addLoan(self,loan):
        self.__loans.append(loan)