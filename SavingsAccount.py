from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def setRate(self,interestRate):
        self.__rate = interestRate
    # no __init__ needed due to inheritance
    

    #add new functionality, getRate()
    def getRate(self):
        return self.__rate
    #overwrite printInfo() to include rate.
    def printInfo(self):
        # Account <name> has a balance of $<x>
        # Cannot use self.__name in the child class, as self.__name is a prvate variable of a parent
        print("Account {} has a balance of ${} with rate {}".format(self.getName(), self.getBalance(), self.__rate))
    
    def applyInterest(self):
        self._balance += self._balance*self.__rate

if __name__ == '__main__':
    print("Savings Account Test")
    savings = SavingsAccount("Savings",1234)
    savings.deposit(100)
    savings.setRate(0.05)
    savings.printInfo()

    savings.applyInterest()
    savings.printInfo()