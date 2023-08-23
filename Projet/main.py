from utils import *

library = Library()
logged_in = False
while not logged_in:
    role = input('Admin or User:').lower()

    if role == 'admin':
        logged_in = admin_login()
        if not logged_in:
            break
        while True:
            action_admin = input('What do you want? Display/Add user/Add book/Search/Edit/Remove/Exit: ').lower()
            
            if action_admin =='display':
                library.display()
            
            elif action_admin =='add user':
                try:
                    fname = input("Fisrt name: ").title()
                    lname = input("Last name: ").title()
                    email = is_valid_email(input("Email: "))
                    phone = is_valid_phone_number(input("Phone number: "))
                    library.add_user(fname, lname, email, phone)
                    print("Added")
                except:
                    print('Please check informations')
            
            elif action_admin =='add book':
                name = input("Title: ").title()
                author = input("Author: ")
                language = input("Language: ").title()
                field = input("Field: ").title()
                publisher = input("Publisher: ").title()
                pub_date=input("Publication date: ")
                edition = input("Edition: ")
                available = 'True'
                library.add_book(name, author, language, field, publisher, pub_date, edition, available)
                print("Added")

            elif action_admin =='search':
                name = input("Enter the name for searching: ").lower()
                results = library.search(name)
                for book_id, name, author, language, field, publisher, pub_date, edition, available in results:
                    print(f"{book_id}: {name}/{author}/{language}/{field}/{publisher}/{pub_date}/{edition}/{available}")
                
            elif action_admin =='edit':
                id = int(input("Enter your book id to edit: "))
                library.edit(id)
                print(f"Edited {id}!")

            elif action_admin == 'remove':
                id = int(input("Enter your book id to remove: "))
                library.remove(id)
                print(f"Removed {id}!")
            
            elif action_admin=="":
                pass
            
            elif action_admin=="exit":
                break
            
            else:
                print(f"{action_admin}: command not found!")

    elif role == 'user':
        logged_in = user_login()
        if not logged_in:
            break
        while True:
            action_user = input('What do you want? Display/Search/Borrow/Return/Exit: ').lower()
        
            if action_user =='display':
                library.display()

            elif action_user =='search':
                            name = input("Enter the name for searching: ").lower()
                            results = library.search(name)
                            for book_id, name, author, language, field, publisher, pub_date, edition, available in results:
                                print(f"{book_id}: {name}/{author}/{language}/{field}/{publisher}/{pub_date}/{edition}/{available}")
            
            elif action_user =='borrow':
                id_user = input("Your id: ")
                id_book = input("Book id: ")
                bname = input("Book name: ")
                library.borrow_book(id_book, id_user, bname)

            elif action_user =='return':
                id_borrow = input("Borrow id: ")
                id_book = input("Book id: ")
                library.return_book(id_borrow, id_book)

            elif action_user =="":
                pass

            elif action_user =="exit":
                break
            else:

                print(f"{action_user}: command not found!")

    else:
        print('Your role NOT found!')
        