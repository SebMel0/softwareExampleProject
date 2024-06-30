idCounter = 0
class Book: 
    def __init__(self,author,title,category):
        global idCounter
        self.__author = author
        self.__title = title
        self.setCategory(category)
        self.__id = idCounter
        idCounter += 1

    # verify that the category is "valid"
    def setCategory(self,category):
            # non-fiction, fiction, reference
            if category in ['non-fiction','fiction','reference']:
                 self.__category = category
            else:
                 print("Error unknown category")
                 self.__category = 'unknown'

    # display book info
    def display(self):
        #title, author, category, id
        print(f"Title:{self.__title}, Author: {self.__author}, Category: {self.__category}, id: {self.__id}")
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.___title
    
    def getAuthor(self):
        return self.__author


# TEST
if __name__ == "__main__":
    new_novel = Book(title="Philosopher's Stone", author="J.K. Rowling",category="fiction")
    new_novel.display()