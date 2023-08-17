# Book Collection Organization
- program that organizes different book objects into a collection
- collection contains head reference for Ordered Linked List
- nodes are ordered by author name (lexicographical and alphabetical order)
  - nodes are also organized by year published and title
- unit tests are included to verify implementation
- Book.py: contains class definition, overloads operators
- BookCollectionNode.py: contains class definitions for the node of the collection
  - returns the next data, current data, sets and updates the data with the newData parameter
  - updates the node's next reference with next parameter

- organizes the data of books by inserting the Book in the correct place based on certain order
- books can be returned based on factors such as a specific author 
