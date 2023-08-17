from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode

# Book.py Tests
b = Book("Blue Banisters", "Del Rey, Lana", 2000)
c = Book("Violet Bent Backwards", "Del Rey, Lana", 2019)
b2 = Book("All About Love", "Hooks, Bell",)
c2 = Book("Crying in H Mart","",2021)
c3 = Book("Candy Necklace", "Grant, Lizzy", 2023)

def test_getBookDetails():
    assert b.getTitle() == "Blue Banisters"
    assert b.getAuthor() == "Del Rey, Lana"
    assert b.getYear() == 2000
    assert b.getBookDetails() == ("Title: Blue Banisters, Author: Del Rey, Lana, Year: 2000")
    assert c.getBookDetails() == ("Title: Violet Bent Backwards, Author: Del Rey, Lana, Year: 2019")
    
    assert b2.getTitle() == "All About Love"
    assert b2.getAuthor() == "Hooks, Bell"
    assert b2.getYear() == None # checks for no year 
    assert c2.getAuthor() == "" # tests for no author
    assert b2.getBookDetails() == ("Title: All About Love, Author: Hooks, Bell, Year: None")
    assert c2.getBookDetails() == ("Title: Crying in H Mart, Author: , Year: 2021")

def test___gt__():
    assert b.__gt__(c) == False # checks if the year > year of other
    assert b2.__gt__(c2) == True
    assert c2.__gt__(b) == False
    assert c.__gt__(b2) == False
    assert c3.__gt__(c) == True
    assert c2.__gt__(b2) == False
    

# BookCollectionNode.py Tests
b3 = BookCollectionNode("Norman F Rockwell, LDR")
b4 = BookCollectionNode("Let the Light In, LDR")
b5 = BookCollectionNode("Margaret, ft Bleachers")
b6 = BookCollectionNode("Happiness is a Butterfly")

def test_getData():
    assert b3.getData() == ("Norman F Rockwell, LDR")
    b3.setData("Peppers, LDR ft. Tommy Genesis")
    assert b3.getData() == ("Peppers, LDR ft. Tommy Genesis")
    b4.setData("Shades of Cool")
    assert b4.getData() == ("Shades of Cool")
    assert b5.getData() == ("Margaret, ft Bleachers")
    b5.setData("Lust for Life")
    assert b5.getData() == ("Lust for Life")

def test_getNext():
    b3.setNext(b4)
    b4.setNext(b5)
    b5.setNext(b6)
    assert b3.getNext() == b4
    assert b4.getNext() == b5
    assert b5.getNext() == b6

# BookCollection.py Tests
b0 = Book("Cujo", "King, Stephen", 1981)
b7 = Book("Hunger Games", "Collins",2016)
c4 = Book("Taco Truck x VB", "Del Rey, Lana",2034)
c5 = Book("A&W", "Grant, Lizzy", 2043)
b8 = Book("Fishtail", "Del Rey, Lana", 1977)
b10 = Book("Flipside", "Grant, Lizzy", 1977)
bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b7)
bc.insertBook(c4)
bc.insertBook(c5)
bc.insertBook(b8)
bc.insertBook(b10)
bc2 = BookCollection()
bc2.insertBook(b0)
bc2.insertBook(c5)
bc2.insertBook(b10) 

def test_BookCollection():
    # tests for isEmpty, getNumberOfBooks, insertBook
    bc = BookCollection()
    assert bc.isEmpty() == True
    bc.insertBook(b7)
    assert bc.getNumberOfBooks() == 1
    assert bc.isEmpty() == False
    bc.insertBook(c4)
    bc.insertBook(c5)
    assert bc.getNumberOfBooks() == 3

def test_getBooksByAuthor():
    assert bc.getBooksByAuthor("DEL REY, lANa") == "Title: Fishtail, Author: Del Rey, Lana, Year: 1977\nTitle: Taco Truck x VB, Author: Del Rey, Lana, Year: 2034\n"
    assert bc.getBooksByAuthor("GrANt, liZZY") == "Title: Flipside, Author: Grant, Lizzy, Year: 1977\nTitle: A&W, Author: Grant, Lizzy, Year: 2043\n"
    assert bc.getBooksByAuthor("Collins") == "Title: Hunger Games, Author: Collins, Year: 2016\n"

def test_removeAuthor():
    bc.removeAuthor("King, Stephen")
    bc.removeAuthor("Collins")
    assert bc.getBooksByAuthor("COLLINS") == ""
    assert bc.getBooksByAuthor("KiNg, StEPhen") == ""
    
def test_getAllBooksIncollection():
    assert bc2.getAllBooksInCollection() == "Title: Flipside, Author: Grant, Lizzy, Year: 1977\nTitle: A&W, Author: Grant, Lizzy, Year: 2043\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    bc2.removeAuthor("KiNg, stEpHen")
    assert bc2.getAllBooksInCollection() == "Title: Flipside, Author: Grant, Lizzy, Year: 1977\nTitle: A&W, Author: Grant, Lizzy, Year: 2043\n"
    assert bc.getAllBooksInCollection() == "Title: Fishtail, Author: Del Rey, Lana, Year: 1977\nTitle: Taco Truck x VB, Author: Del Rey, Lana, Year: 2034\nTitle: Flipside, Author: Grant, Lizzy, Year: 1977\nTitle: A&W, Author: Grant, Lizzy, Year: 2043\n"

def test_recursiveSearchTitle():
    bc.recursiveSearchTitle("Fishtail", bc.head)
    assert bc.recursiveSearchTitle("FISHTAIL", bc.head) == True
    assert bc.recursiveSearchTitle("CUJo", bc.head) == False
    bc.recursiveSearchTitle("Taco Truck x VB", bc.head)
    assert bc.recursiveSearchTitle("Taco Truck x VB", bc.head) == True
    


