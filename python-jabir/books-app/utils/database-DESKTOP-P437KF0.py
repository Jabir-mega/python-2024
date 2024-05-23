# import sqlite3 module 
import sqlite3

# boo store database
db = 'booksstore.db'

# A function to create the books table 
def create_books_table():
    # create the database connection
    connection = sqlite3.connect(db)
    #create  the create table query 
    query = """CREATE TABLE IF NOT EXISTS books (book_id INTERGER UNIQUE NOT NULL PRIMARY KEY,
    title char(50),
    author char(50),
    read INTERGER NOT NULL
    );
    """
    # create the cursor object
    cursor = connection.cursor()
    # execute the query
    cursor.execute(query)
    # commit the changes
    connection.commit()
    # close the connection
    connection.close()

# create an empty list to store the books
books = [
    # { 'Title' : 'Modern Javascript',
    #     'Author' : 'Jabir Ali',
    #     'Read': False
    # } 
    # {
    #     'Tilte' : 'Clean Code'
    #     'Author' : 'Jones Bones'
    #     'Read' : False
    # }   
]

# create a function to add books to the list
def add_book(title, author):
    # create the database connection
    connection = sqlite3.connect(db)
    #create  the add book query 
    query = "INSERT INTO books (book_id, title, author, read) VALUES (?, ?, ?, ?)"
    # create the cursor object
    cursor = connection.cursor()
    # execute the query
    cursor.execute(query, [1, title, author, 0])
    # commit the changes
    connection.commit()
    # close the connection
    connection.close()
# create a function to get all the books from the list
def get_all_books():
     # create the database connection
    connection = sqlite3.connect(db)
    #create  the display book query 
    query = "SELECT * FROM books"
    # create the cursor object
    cursor = connection.cursor()
    # execute the query
    cursor.execute(query)
    # retrive all books from db
    book = cursor.fetchall()
    # close the connection
    connection.close()
    # return books list
    return book
    
# create a function to mark a book as read
def mark_book_read(title):
      # create the database connection
    connection = sqlite3.connect(db)
    #create  the update book query 
    query = "UPDATE books SET read = ? WHERE title = ?"
    # create the cursor object
    cursor = connection.cursor()
    # execute the query
    cursor.execute(query, [1, title])
    # commit the changes
    connection.commit()
    # close the connection
    connection.close()

# create a function to delete a book

def delete_book(title):
        pass

#