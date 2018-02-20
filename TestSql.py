from Library.Sql import*

print("""
Welcome Library Program

1.Show Books
2.Control Books
3.Add Books
4.Delete Books
5.Quit
""")

library=Library()


while True:

    choice1=input("Select your choice:")

    if choice1=="5":

        break

    elif choice1=="1":

        library.show_books()

    elif choice1=="2":

        library.control_books()

    elif choice1=="3":

        library.add_book()

    elif choice1=="4":

        library.delete_book()

    else:

        print("Wrong Choice!!")
