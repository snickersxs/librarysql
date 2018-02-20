import sqlite3

import time

class Book():

    def __init__(self,name,author,publisher,type,year,page):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.type = type
        self.year = year
        self.page = page
    def __str__(self):

        return "Name: {}\nAuthor: {}\nPublisher: {}\nType: {}\nYear: {}\nPage: {}".format(self.name,self.author,self.publisher,self.type,self.year,self.page)

class Library():

    def __init__(self):
        self.connect_database()

    def connect_database(self):
        self.connect = sqlite3.connect("librarydatabase.db")

        self.cursor = self.connect.cursor()

        data = "CREATE TABLE IF NOT EXISTS books (Name TEXT,Author TEXT,Publisher TEXT,Type TEXT,Year INT,Page INT)"

        self.cursor.execute(data)

        self.connect.commit()

    def unconnect_database(self):
        self.connect.close()

    def show_books(self):

        data="Select *From books"

        self.cursor.execute(data)

        books=self.cursor.fetchall()

        if len(books)==0:
            print("No books to show...")

        for i in books:
            book=Book(i[0],i[1],i[2],i[3],i[4],i[5])
            print(book)

    def control_books(self):
        while True:
            print("""
            1.By Name
            2.By Author
            3.By Publisher
            4.By Type
            5.By Year
            6.By Page
            0.Exit
            """)
            choice=int(input("Select your choice"))
            if choice==1:
                data = "Select *from books where Name=?",(input("Enter Name: \n"),)
                self.cursor.execute(data)
                books=self.cursor.fetchall()
                if len(books)==0:
                    print("No book.")
                else:
                    for i in books:
                        book = Book(i[0], i[1], i[2], i[3], i[4], i[5])
                        print(book)

            elif choice==2:
                cauthor = input("Enter Author: \n")
                data = "Select *from books where Author=?"
                self.cursor.execute(data,(cauthor,))
                books=self.cursor.fetchall()
                if len(books)==0:
                    print("No book.")
                else:
                    for i in books:
                        book = Book(i[0], i[1], i[2], i[3], i[4], i[5])
                        print(book)
                pass

            elif choice==3:
                ppublisher=input("Enter Publisher: \n")
                data = "Select *from books where Publisher=?"
                self.cursor.execute(data,(ppublisher,))
                books=self.cursor.fetchall()
                if len(books)==0:
                    print("No book.")
                else:
                    for i in books:
                        book = Book(i[0], i[1], i[2], i[3], i[4], i[5])
                        print(book)
                pass
            elif choice==4:
                ttype=input("Enter Type: \n")
                data = "Select *from books where Type=?"
                self.cursor.execute(data,(ttype,))
                books=self.cursor.fetchall()
                if len(books)==0:
                    print("No book.")
                else:
                    for i in books:
                        book = Book(i[0], i[1], i[2], i[3], i[4], i[5])
                        print(book)
                pass
            elif choice==5:
                yyear=int(input("Enter Year: \n"))
                data = "Select *from books where Year=?"
                self.cursor.execute(data,(yyear,))
                books=self.cursor.fetchall()
                if len(books)==0:
                    print("No book.")
                else:
                    for i in books:
                        book = Book(i[0], i[1], i[2], i[3], i[4], i[5])
                        print(book)
                pass
            elif choice==6:
                ppage=int(input("Enter Page: \n"))
                data = "Select *from books where Page=?"
                self.cursor.execute(data,(ppage,))
                books=self.cursor.fetchall()
                if len(books)==0:
                    print("No book.")
                else:
                    for i in books:
                        book = Book(i[0], i[1], i[2], i[3], i[4], i[5])
                        print(book)
                pass
            elif choice==0:
                break
            else:
                print("Wrong choice control book")


    def add_book(self):
        name=input("Name: ")

        author=input(("Author: "))

        publisher=input("Publisher: ")

        type=input(("Type: "))

        year=int(input("Year: "))

        page=int(input("Page: "))

        book=Book(name,author,publisher,type,year,page)

        data="Insert into books VALUES (?,?,?,?,?,?)"

        self.cursor.execute(data,(book.name,book.author,book.publisher,book.type,book.year,book.page))

        self.connect.commit()

    def delete_book(self):

        name=input("Name: ")

        data="Delete from books where NAME =?"

        self.cursor.execute(data,(name,))

        self.connect.commit()

        print("Deleted.")


