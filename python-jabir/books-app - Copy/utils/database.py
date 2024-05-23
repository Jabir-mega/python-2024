# create an empty list to store the books
# books = [
#     { 'Title' : 'Modern Javascript',
#         'Author' : 'Jabir Ali',
#         'Read': False
#     } 
#     {
#         'Tilte' : 'Clean Code'
#         'Author' : 'Jones Bones'
#         'Read' : False
#     }   
# ]

#     #     'Title' : 'Modern Javascript', 
#     #     'Author': 'Jabir Ali',
#     #     'Read' : False
#     #   }
#     #   {
#     #      'title' : 'clean Code',
#     #     'Author' : 'Robert C.Martin',
#     #     # 'Read' : False
# # create a function to add books to the list
# def add_book(title, author):
#     books.append({
#         'title': title,
#         'author': author,
#         'read': False
#     })
# # create a function to get all the books from the list
# def get_all_books():
#     return books
# # create a function to mark a book as read
# def mark_book_read(title):
#     for book in books:
#         if book['title'] == title:
#             book['read'] = True
# # create a function to delete a book
# def delete_book(title):
#     for book in books:
#         if book['title'] == title:
#             books.remove(book)

#  create an empty list to store the books

books = []

# create a function to add books to the list

def add_book(title, author):

    books.append({

        'title': title,

        'author': author,

        'read': False

    })

# create a function to get all the books from the list

def get_all_books():

    return books

# create a function to mark a book as read

def mark_book_read(title):

    for book in books:

        if book['title'] == title:

            book['read'] = True

# create a function to delete a book

def delete_book(title):

    pass

