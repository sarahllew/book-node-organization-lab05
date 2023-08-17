
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        '''returns the total number of Books(int) in collection'''
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        '''inserts a Book in the appropriate place...
            basd on 1) author (alpha)
            2) year of publication
            3) title (lexicographical)'''
        current = self.head
        previous = None
        stop = False

        # finding the correct place
        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        '''returns a str containing all the book
            details by a specific author, each book will be in its own line
         get books whose author matches'''
        current = self.head
        details = ""
        while current != None:
            if current.getData().getAuthor().upper() == author.upper():
                details += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return details

    def getAllBooksInCollection(self):
        '''returns a str containing all the details of all
            books in Book Collection, each book is in its own line'''
        current = self.head
        details = ""
        while current != None:
            details += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return details

    def removeAuthor(self, author):
        '''removes all Books written by specified author'''
        current = self.head
        previous = None
        found = False
        if current == None: 
            return
        while not found: 
            if current.getData().getAuthor() == None:
                return
            if current.getData().getAuthor().upper() == author.upper():
                found = True
            else:
                previous = current
                current = current.getNext()

        # another while loop to remove the nodes in between the nodes you want to delete
        while current != None and current.getData().getAuthor().upper() == author.upper():
            current = current.getNext()
                
        if found == True and previous == None:
            self.head = current

        if found == True and previous != None:
            previous.setNext(current)

    def recursiveSearchTitle(self, title, bookNode):
        '''searches the BookCollection for a specific title passed.
            method returns True if a Book in BookCollection has the same
            title as title parameter, and return False otherwise.
                - method takes in a reference to a BookCollectionNode object
                (bookNode).
                - initial call to recursiveSearchTitle passes in the head of
                BookCollection since that's the starting point.
                - then recursively search through the sub parts by recursively
                referring to the next BookCollectionNode in BookCollection that
                needs to be searched if the Book in bookNode does not have the title.'''

        if bookNode == None:
            return False
        else:
            if bookNode.getData().getTitle().upper() == title.upper():
                return True
            else:
                return self.recursiveSearchTitle(title,bookNode.getNext())
                
          
## getBooksByAuthor()
##b0 = Book("Cujo", "King, Stephen", 1981)
##b1 = Book("The Shining", "King, Stephen", 1977)
##b2 = Book("Ready Player One", "Cline, Ernest", 2011)
##b3 = Book("Rage", "King, Stephen", 1977)

##bc = BookCollection()
##bc.insertBook(b0)
##bc.insertBook(b1)
##bc.insertBook(b2)
##bc.insertBook(b3)
##print(bc.getBooksByAuthor("KING, Stephen"))

## getAllBooksInCollection()
##b0 = Book("Cujo", "King, Stephen", 1981)
##b1 = Book("The Shining", "King, Stephen", 1977)
##b2 = Book("Ready Player One", "Cline, Ernest", 2011)
##b3 = Book("Rage", "King, Stephen", 1977)
##
##bc = BookCollection()
##bc.insertBook(b0)
##bc.insertBook(b1)
##bc.insertBook(b2)
##bc.insertBook(b3)
##print(bc.getAllBooksInCollection())

##b0 = Book("Cujo", "King, Stephen", 1981)
##b1 = Book("The Shining", "King, Stephen", 1977)
##bc = BookCollection()
##bc.insertBook(b0)
##bc.insertBook(b1)
##bc.recursiveSearchTitle("CUJO", bc.head)
##assert bc.recursiveSearchTitle("CUJO", bc.head) == True
##assert bc.recursiveSearchTitle("Twilight", bc.head) == False



