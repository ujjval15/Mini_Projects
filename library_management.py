import sys
class Library:
    
    def __init__(self, books):
        self.books = books
    def dis_books(self):
        for book in self.books:
            print(book)
    def lend_book(self, a):

        choice1 = input("Enter the name of the book you want to borrow : ")
        if choice1 in self.books:
            self.books.remove(choice1)
            print (f"{choice1} has successfully been borrowed by you.")
        else:
            print(f"Library does not contain this book.\n This book has been borrowed by {choice4}")
    def add_book(self):
        
        choice2 = input("Enter the book you want to add in this library : ")
        self.books.append(choice2)
        print(f"Thanks for donating {choice2}")
    def ret_book(self):
        
        choice3 = input("Enter the name of the book you want to return : ")
        self.books.append(choice3)
        print(f"Hello {choice4} You have successfully returned your book.")
    
if __name__ == '__main__':
    print("====WELCOME TO MY LIBRARY====")
    library = Library(["Python for beginners", "Learn C", "Java programming"])
    choice4 = input("Please Enter Your Name: ")
    
    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t WELCOME {choice4} What would you like to do")
    lst = []
    lst.append(choice4)
    a = False
    while a == False:
        print("1>> Display available books\n"
              "2>> Lend a book\n"
              "3>> Add a book\n"
              "4>> Return a book\n"
              "5>> Number of customers visited\n"
              "6>> Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            print("Available books are : ")
            library.dis_books()
        elif choice == 2:
            print("Available books are : ")
            library.lend_book(library.dis_books())
        elif choice == 3:
            library.add_book()
        elif choice == 4:
            library.ret_book()
        elif choice ==5:
            print(lst)
        else:
            print("Thanks for visiting")
            sys.exit()