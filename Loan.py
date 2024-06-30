from datetime import datetime
class Loan:
   
    
    
    def display(self):
        print(f"Book ID: {self.__bookID}")
        print(f"Borrower ID: {self.__borrowerID}")
        print(f"Due Date: {self.__dueDate}")
    
    # getters
    def getID(self):
        return self.__bookID
    
    def getBookID(self):
        return self.__bookID

    def getBorrowerID(self):
        return self.__borrowerID
    
    