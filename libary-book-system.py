# Library Book System

#& The idea: You're modeling a small library where books can be checked out and returned, and you track who currently has what.

status = False

#* Books Class
class book:
    def __init__(self, title, author, rating, availability):
        self.title = title
        self.author = author
        self.rating = rating
        self.availability = availability

    # checkout a book
    def checkout_book(self):
        # check it out from the libary
        self.availability = False

    # return a book
    def return_book(self):
        self.availability = True

#* New Books
book1 = book('The Alchemist', 'Paulo Coelho', 8, True)
book2 = book('Broken', 'Fatima Bala', 7.5, False)
book3 = book('Hafsatu Bebi', 'Fatima Bala', 9, True)
book4 = book('Atomic Habits', 'James Clear', 10, False)

libary = [book1, book2, book3, book4]

#? view all books function
def view_books():
    print('All books in the Libary')
    print('\n')
    for book in libary:
        print(f'Title: {book.title}')
        print(f'Author: {book.author}')
        print(f'rating: {book.rating} / 10')
        if book.availability:
            print('Available')
        else:
            print('Not Available')
        print('\n')

#? Checkout book function
def checkout_or_return(action):
    print('\n')
    # get name of book from user
    if action == '2':
        book_title = input('Title of the book you want to checkout: ')
    else:
        book_title = input('Title of the book you want to return: ')

    # toggle if book is in libary
    in_libary = False

    # check if book is in libary and is available
    for book in libary:
        if book_title.lower() == book.title.lower():
            in_libary = True
            print('\n')
            # check for books availability
            # chechout
            if action == '2':
                if book.availability:
                    print(f'{book.title} by {book.author} has been succesfully checked out')
                    book.checkout_book()
                else:
                    print(f'{book.title} by {book.author} has already been checked out')
            else:
            # return
                if book.availability:
                    print(f'{book.title} by {book.author} has already been returned')
                else:
                    print(f'{book.title} by {book.author} has been succesfully returned')
                    book.return_book()
            break

    print('\n')

    # handle book no in liabry
    if not in_libary:
        print(f'{book_title} is not in our Libary')
        print('\n')

# Start program
while not status:
    print('Welcome to the Libary Menu')
    print('1. View all books')
    print('2. Checkout a book')
    print('3. Return a book')
    print('4. Exit')

    user_input_valid = False
     
    # Take user input
    user_input = (input('Select from 1 - 4: '))

    # validate user input
    while not user_input_valid:
        if user_input in ['1', '2', '3', '4']:
            user_input_valid = True
        else:
            user_input = input('Please Choose from 1 - 4: ')

    # run function based on
    if user_input_valid == True:
        if user_input == '1':
            view_books()
        elif user_input == '2' or user_input == '3':
            checkout_or_return(user_input)
        elif user_input == '4':
            status = True
            break
        
