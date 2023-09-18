class Library:

    def __init__(self,booklist):
        self.books = booklist
       

    def Display_Avalible_Book(self):
        print("\nThe avalibel Books are: ")
        for index,book in enumerate(self.books):
            print(index,book)
        

    def Borrow_Book(self,bookName):
        if bookName in self.books:
            print("******you have been issued {}. keep it safe, and return within 30 days.******".format(bookName))
            self.books.remove(bookName)
        else:
            print("******Sorry! This book is not avalible yet or has already issued to someone else please wait until the book is avalibe.******")
        

    def Return_Book(self,bookname):
            self.books.append(bookname)
            print("******Thanks! for returning this book.Hope enjoyed reading it! have a great day ahade!****** ")


    
    def ADD_Book(self,bookname):
        self.books.append(bookname)
        print("******Thanks! for Adding this book in \"CHUDHARY LIBRARY\"****** ") 
        print("Plese Enter a valid name")



class Student:
    def Request_Book(self):
        self.book = input("Enter the name of the book you want to borow: ")
        return self.book        
    
    def Return_book(self):
        self.book = input("Enter the name of the book you want to return: ")      
        return self.book

    def Add_Book(self):
        self.book = input("Enter the name of the book you want to add: ")
        return self.book


if __name__ == "__main__":
    Chudharylibrary = Library(["RICH DAD POOR DAD","THINK AND GROW RICH","EAT THAT FROG","KISS THAT FROG","HOW TO TALK TO ANYONE","YES YOU CAN","ATMOIC HABBIT","THE POWER OF YOUR SUBCONSIOUS MIND"])

    student = Student()



    while True:
        welcome_msg = '''\n\n  ===== WELCOME TO CHUDHARY LIBRARY =====
        *Please choose an option:
        1. press "1" for list all books avalibel in library.
        2. press "2" for request a book.
        3. press "3" for return a book.
        4. press "4" for add a book.
        5. press "5" Exit the library.
'''
        try:
            print(welcome_msg)
            user = int(input("Enter a choise: "))
            if user == 1:
                Chudharylibrary.Display_Avalible_Book()
            elif user == 2:
                Chudharylibrary.Borrow_Book(student.Request_Book())
            elif user == 3: 
                Chudharylibrary.Return_Book(student.Return_book())
            elif user == 4:
                Chudharylibrary.ADD_Book(student.Add_Book())
            elif user == 5:
                exit()
            else:
                print("Please enter a valid choise.")
        except Exception as e:
            print("Exception occur: ",e)


        
