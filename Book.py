'''contains the definition of a book'''

class Book:
    '''Book class definition that has the attributes of a book'''
    def __init__(self, title = "", author ="" , year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return("Title: {}, Author: {}, Year: {}".format(self.title,self.author,self.year))

    def __gt__(self, other):
        if self.author.upper() > other.author.upper():
            return True
        elif self.author.upper() == other.author.upper():
            if self.year > other.year:
                return True
            elif self.year == other.year:
                if self.title.upper() > other.title.upper():
                    return True
        return False
        
'''
b = Book("Ready Player One", "Cline, Ernest", 2011)
print(b.getBookDetails())
'''

