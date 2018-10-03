# Creation of the parent class Library Item
class LibraryItem:
    # this parent class only holds the ID of each item, no other information
    def __init__(self, library_id):
        self.library_id = library_id


    #def getLibraryID(self):
        #return self.__library_id

# Creation of the child class Periodical
class Periodical(LibraryItem):

    def __init__(self, library_id, title, editor, pub_year, volume, issue):
        LibraryItem.__init__(self, library_id)
        self.__title = title
        self.__editor = editor
        self.__pub_year = pub_year
        self.__volume = volume
        self.__issue = issue

# the class attributes are encapsulated
# we define some public methods to access them
    def getPTitle(self):
        return self.__title.lower()

    def getEditor(self):
        return self.__editor

    def getPPubYear(self):
        return self.__pub_year


    def __str__(self):
        return "Library Code: {}, Title: {}, Editor: {}, Issue: {}".format(self.library_id,self.__title,self.__editor, self.__issue)


# Creation of the child class Book
class Book(LibraryItem):
    def __init__(self, library_id, isbn, title, author, pub_year):
        LibraryItem.__init__(self, library_id)
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__pub_year = pub_year
        self.__status = "Available"
        # when a book object is created, its status is automatically set to 'Available'

    def __str__(self):
        return "Library Code: {}, ISBN: {}, Title: {}, Author: {}, Publication Year: {}, Status: {}".format(self.library_id,self.__isbn,self.__title,self.__author, self.__pub_year, self.__status)

# the class attributes are encapsulated
# we define public methods to access them
# we define methods to convert the title and the author to lower case  to handle user input
    def getTitle(self):
        return self.__title.lower()

    def getCaseTitle(self):
        return self.__title

    def printTitle(self):
        print(self.getCaseTitle())

    def getAuthor(self):
        return self.__author.lower()

    def getISBN(self):
        return self.__isbn

    def getYear(self):
        return self.__pub_year

# we define methods to change the status of the book when loaned and returned
    def changeStatusToLoaned(self):
        self.__status = "Loaned"

    def changeStatusToAvailable(self):
        self.__status = "Available"

# Creation of the class Library
class Library:

    # the Library class contains a list of Book objects, Periodical objects and User objects
    def __init__(self):
        self.books = []
        self.periodicals = []
        self.users = []

    # Methods to print all the items that the Library holds
    # we first iterate over the list of books and then over the list of periodicals
    def printItems(self):
        print("Here are the current Library Books:\n")
        for i in self.books:
            print(i)
        print("\n")

        print("Here are the current Library Periodicals:\n")
        for p in self.periodicals:
            print(p)
        print("\n")

    # Methods to print all the users that the Library holds
    # we iterate over the list of users
    # for each user in the Libray, we check and print books they have on loan
    def printUsers(self):
        print("Here are the current Library Users:\n")
        for j in self.users:
            print(j)

            if j.on_loan==[]:
                print("Books on loan: None")
            else:
                print("Books on loan:")
                j.getLoanedBookTitle()

            print("\n")

# we define methods to add and remove books, periodicals and users from the library
# to add or remove these objects from the Library, we simply append or remove them from the list they belong to

    def addBook(self, b):
        self.books.append(b)

    def addPeriodical(self, p):
        self.periodicals.append(p)

    def removeBook(self,b):
        self.books.remove(b)

    def removePeriodical(self,p):
        self.periodicals.remove(p)

    def addUser(self,u):
        self.users.append(u)

    def removeUser(self,u):
        self.users.remove(u)

# Creation of the class User
class User:
    def __init__(self, user_id, name, address):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.on_loan = []
        # when a user object is created, they have no book on loan so the list containing this information is by default empty

    def __str__(self):
        return "User ID: {}, Name: {}, Address: {}".format(self.user_id,self.name, self.address)

# we define a method to add a book to the list of books on loan for a user
# within this method, we also change the status of the book loaned to "Loaned"
    def addOnLoan(self,b):
        self.on_loan.append(b)
        b.changeStatusToLoaned()

# we define a method to return a book, i.e. we remove a book from the list of books on loan for a user
# within this method, we also change the status of the book returned to "Available"
    def returnLoan(self,b):
        self.on_loan.remove(b)
        b.changeStatusToAvailable()

# method to access a book title from the list of books on loan for a user, as the title attribute is encapsulated
    def getLoanedBookTitle(self):
        for b in self.on_loan:
            b.printTitle()

# Library system functions

# Creating a new User object via user input
# throws an error if input is empty
def userCreation(cls):

    try:
        while True:
            u_id=input('user_id')
            name = input('name')
            address = input('address')
            if u_id.strip() == "":
                print("ID cannot be empty!")
                break
            elif name.strip() == "":
                print("Name cannot be empty!")
                break

            elif address.strip() == "":
                print("Address cannot be empty!")
                break
            else:
                u = cls(u_id, name, address)
                L.addUser(u)
            break
    except ValueError:
        print("Incorrect input")
        backToMainMenu()

# Creating a new Book object via user input
# throws an error if input is empty
# ISBN must be 13-digit long
def bookCreation(cls):

    try:
        while True:
            # we define the count variable to check the iSBN input
            count = 0
            # we prompt the user to enter the new book object attributes
            book_id= input("Enter the book ID")
            isbn_user = input("Enter the book ISBN")
            title = input("Enter the book title")
            author = input("Enter the author")
            pub_year = int(input("Enter the Publication Year"))

            # checks if the user input contains 13 characters.
            while True:
                for i in isbn_user:
                    if chr(47) < i < chr(58):
                        count += 1
                if count == 13:
                    break
                else:

                    break

            # checking for empty input. If input is empty, the book object is not created
            if book_id.strip() == "":
                print("ID cannot be empty!")

            elif isbn_user == "":
                print("ISBN cannot be empty!")
            elif count != 13:
                print("invalid ISBN")

            elif title.strip() == "":
                print("Title cannot be empty!")

            elif author.strip() == "":
                print("Author cannot be empty!")

            elif pub_year == "":
                print("Address cannot be empty!")

            # if no empty input, creates new book
            else:
                b = cls(book_id, isbn_user, title, author, pub_year)
                L.addBook(b)
                print("A new book has been added")
            break
    except ValueError:
        print("Invalid Input")
        backToMainMenu()

# Creating a new Periodical object via user input
# throws an error if input is empty

def periodicalCreation(cls):

    try:
        while True:
            p_id= input("Enter the periodical ID")
            title = input("Enter the periodical title")
            editor = input("Enter the editor")
            pub_year = int(input("Enter the Publication Year"))
            volume = int(input("Enter the volume"))
            issue = int(input("Enter the issue"))
            if p_id.strip() == "":
                print("Periodical ID cannot be empty!")
            elif title.strip() == "":
                print("Title cannot be empty!")
            elif editor.strip() == "":
                print("Editor cannot be empty!")
            elif pub_year == "":
                print("Publication year cannot be empty!")
            elif volume == "":
                print("Volume cannot be empty!")
            elif issue == "":
                print("Issue cannot be empty!")
            else:
                p = cls(p_id, title, editor, pub_year, volume,issue)
                L.addPeriodical(p)
                print("A new periodical has been added")
            break
    except:
        print("Invalid Input")
        backToMainMenu()

# Removing a book for the Library
# a book can only be removed from Library using its ID
# if book id entered by user doesn't not match any book in the Library, throws an error message
def bookDeletion():
    try:
        b_del = input("Enter library ID")

        if b_del != "":
            for b in L.books:
                if b_del==b.library_id:
                    L.removeBook(b)
                    print( "A book was deleted")
                else:
                    print("Book ID not found")
                    backToMainMenu()
        else:
            print("Input cannot be empty")
    except ValueError:
        print("Invalid Input")
        backToMainMenu()

# Removing a periodical from for the Library
# a periodical can only be removed from Library using its ID
# if periodical id entered by user doesn't not match any book in the Library, throws an error message
def periodicalDeletion():
    try:
        p_del=input("Enter Periodical ID")

        if p_del !="":
            for p in L.periodicals:
                if p_del==p.library_id:
                    L.removePeriodical(p)
                    print("A periodical has been deleted")
                else:
                    print("Periodical ID not found")
        else:
            print("Input cannot be empty")
            backToMainMenu()
    except:
        print("Invalid input")
        backToMainMenu()

# Removing a user for the Library
# a user can only be removed from Library using its ID
# if user id entered by user doesn't not match any book in the Library, throws an error message
def userDeletion():
    try:
        u_del=input("Enter User ID")

        if u_del != "":
            for u in L.users:
                if u_del==u.user_id:
                    L.removeUser(u)
                else:
                    print("User ID not found")
        else:
            print("Input cannot be empty")
            backToMainMenu()
    except:
        print("Invalid input")
        backToMainMenu()

# finding item in the library based on user input
# for books, the user can use its ID, its title or its author or its ISBN as an input
# for periodicals, the user can use its ID, its title or its editor as an input
# throws an error if the input doesn't match any object's attribute or if the input is empty
def findItem():
    try:
        find=input("What are you looking for?")
        find_lower=find.lower()

        if find_lower.strip() != "":
            for b in L.books:
                if find_lower in b.library_id or find_lower in b.getTitle() or find_lower in b.getAuthor() or find_lower in b.getISBN():
                    print(b)
                    break
            else:
                print("Book not found")

            for p in L.periodicals:
                if find_lower in p.library_id or find_lower in p.getPTitle() or find_lower in p.getEditor():
                    print(p)
                    break
            else:
                print("Periodical not found")
        else:
            print("Your search cannot be empty.")
    except ValueError:
        print("Invalid Input")

# finding a user in the library based on user input
# the user can use its ID, its name or its address as an input
# throws an error if the input doesn't match any user's attribute or if the input is empty
def findUser():
    try:
        find = input("Who are you looking for?")
        find_lower=find.lower()

        if find_lower.strip() != "":
            for u in L.users:
                if find_lower in u.user_id.lower() or find_lower in u.name.lower() or find_lower in u.address.lower():
                    print(u)
                    break
            else:
                print("No user found")
        else:
            print("Your search cannot be empty.")
    except ValueError:
        print("Invalid Input")

# loaning a book based user input
# prompts for user id of the user that wants to loa the book + book id of the book to be loaned
# calls the method addOnLoan to add the book to the list of book on loan for the user + to update the status of the book to "Loaned"
# throws an error if input is empty or book or user is not found
def loanBook():
    try:
        userID = input("Enter User ID: ")
        bookID = input("Enter Book ID: ")
        if userID !="" and bookID !="":
            for u in L.users:
                for b in L.books:
                    if userID == u.user_id:
                        if bookID == b.library_id:
                            u.addOnLoan(b)
                        else:
                            print("Book not found")
                    else:
                        print("User not found")
        else:
            print("Input cannot be empty")
    except ValueError:
        print("Invalid input")
        backToMainMenu()

# returning a book based user input
# prompts for user id of the user that wants to return the book + book id of the book to be returned
# calls the method return Loan to remove the book from the list of books on loan for the user + to update the status of the book to "Available"
# throws an error if input is empty or book or user is not found
def returnBook():
    try:
        userID = input("Enter User ID: ")
        bookID = input("Enter Book ID: ")
        if userID != "" and bookID !="":
            for u in L.users:
                for b in L.books:
                    if userID == u.user_id:
                        if bookID == b.library_id:
                            u.returnLoan(b)
                        else:
                            print("Book not found")
                            break
                    else:
                        print("User not found")
                        break
        else:
            print("Input cannot be empty")
    except ValueError:
        print("Invalid Input")
        backToMainMenu()

# MENU#

def main_menu():
    print("")
    print("### MAIN MENU ###")

    try:
        navigation = int(input(
            "What do you want to do? \n * Enter 1 to display the entire library catalogue \n "
            "* Enter 2 if you want to display the library users \n "
            "* Enter 3 if you want to add or remove an library item \n "
            "* Enter 4 if you want to add or remove an library user \n "
            "* Enter 5 if you want to loan or return a book \n "
            "* Enter 6 if you want to look for an item or a user \n "
            "* Enter 0 if you want to exit the system \n"))
        # user faces seven navigation choices; they can enter an integer between 0 and 6
        # if user chooses between option 3 and 6, programme calls a specific sub-menu with several more choices to make
        # throws an error is input is not valid
        if navigation == 1:
            L.printItems()
            main_menu()
        elif navigation == 2:
            L.printUsers()
            main_menu()
        elif navigation == 3:
            submenu_1()
        elif navigation == 4:
            submenu_2()
        elif navigation==5:
            submenu_3()
        elif navigation==6:
            submenu_4()
        elif navigation==0:
            quit()
    except ValueError:
        print("This is not a valid option. Try entering a digit between 0 and 6 this time!")
        main_menu()

# Back to main menu function
#  After performing an action, the user can choose to exit the system or to go back to the main menu
def backToMainMenu():
    print("###")
    try:
        nav = input("Do you want to go back to the main menu (y/n)?")
        if nav.lower() == "y":
            main_menu()
        elif nav.lower()=="n":
            print("Bye for now!")
            quit()
    except ValueError:
        print("Invalid input. Please enter 'y' or 'no'")
        backToMainMenu()

# SUB-MENUS
# within each sub-menu, we call the relevant functions

# Add or delete a library item
def submenu_1():
    try:
        sub_nav = int(input("Enter 1 to add a Book, 2 to add a Periodical, 3 to remove a Book or 4 to remove a Perdiodical."))
        if sub_nav==1:
            bookCreation(Book)
            L.printItems()
        elif sub_nav==2:
            periodicalCreation(Periodical)
            L.printItems()
        elif sub_nav==3:
            bookDeletion()
            L.printItems()
        elif sub_nav==4:
            periodicalDeletion()
            L.printItems()
        backToMainMenu()
    except ValueError:
        print("This is not a valid option. Try again")
        submenu_1()

# Add or delete a user
def submenu_2():
    try:
        sub_nav = int(input("Enter 1 to add a user or Enter 2 to remove a user"))
        if sub_nav==1:
            userCreation(User)
        elif sub_nav==2:
            userDeletion()
        L.printUsers()
        backToMainMenu()
    except ValueError:
        print("This is not a valid option. Try again")
        submenu_2()

# Loan or return a book
def submenu_3():
    try:
        sub_nav = int(input("Select 1 to loan a Book or select 2 to return a Book."))
        if sub_nav == 1:
            loanBook()
        elif sub_nav == 2:
            returnBook()
        L.printItems()
        L.printUsers()
        backToMainMenu()
    except ValueError:
        print("This is not a valid option. Try again")
        submenu_3()

# Look for an item or a user
def submenu_4():
    try:
        sub_nav = int(input("Enter y to look for a item or enter 2 to look for a user"))
        if sub_nav == 1:
            findItem()
        elif sub_nav == 2:
            findUser()
        backToMainMenu()
    except ValueError:
        print("This is not a valid option. Try again")
        submenu_4()

# Creating some initial objects: 2 books, 2 periodicals, 2 users
book1 = Book("b1", "9780141036144", "1984", "Georges Orwell", 1948)
book2 = Book("b2", "9780434023301", "The Sunlight Pilgrims", "Jenni Fagan", 2016)
periodical1 = Periodical("p1", "Newsweek", "Nancy Cooper", 2018, 18, "2018, March 02")
periodical2 = Periodical("p2", "Rolling Stone", "Jann Wenner", 2018, 18, "2018, April 02")
user1 = User("u1", "Paolo Radaelli", "25 Wintergarden")
user2 = User("u2", "Jane Smith", "45 Saint Mary's Road")


# Creation of Library object
L = Library()

# Adding Books, Periodicals and Users to the Library
L.addBook(book1)
L.addBook(book2)
L.addPeriodical(periodical1)
L.addPeriodical(periodical2)
L.addUser(user1)
L.addUser(user2)

# Launching the main menu
main_menu()