from config_func import *
from datetime import datetime, timedelta
import re
from book import *
from user import *
from person import *
from admin import *

# Check Valid Phone number
def is_valid_phone_number(phone_number):
    pattern = re.compile(r'^0\d{10}$') # regular expression pattern to match 11 digits
    match = pattern.match(phone_number)
    if match:
        return phone_number
    else:
        print(f'Please enter a correct phone number')

# Check Valid Email address   
def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') # regular expression pattern to match email
    match = pattern.match(email)
    if match:
        return email
    else:
        print(f'Please enter a correct email')

# Log in User
def user_login():
    while True:
        firstname = input("Enter your firstname: ")
        lastname = input("Enter your lastname: ")

        # Check if the username and password match an user account in the database
        cursor = cnx.cursor()
        query = "SELECT * FROM User WHERE Firstname = %s AND Lastname = %s"
        values = (firstname,lastname)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            print(f"Dear {firstname} {lastname} Welcome!")
            return True
        else:
            print("WRONG Name or You are not a member of the library.")
            answer = input('If you are an user, Do you want to try again? (y/n)').lower()
            if answer == 'y':
                continue
            else:
                return False


# Log in Admin
def admin_login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username and password match an admin account in the database
        cursor = cnx.cursor()
        query = "SELECT * FROM Admin WHERE Username = %s AND Password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            print("Login successful.")
            return True
        else:
            print("WRONG username or You do NOT have permission to access.")
            answer = input('If you are an admin, Do you want to try again? (y/n)').lower()
            if answer == 'y':
                continue
            else:
                return False
            
class Library:
    def __init__(self):
        self.books=[]

    # Add books to Book table
    def add_book(self, name, author, language, field, publisher, pub_date, edition, available):
      
        mycursor = cnx.cursor()
        lib_book = Book(name, author, language, field, publisher, pub_date, edition, available)
        query = """INSERT INTO Book (Name,
                                    Author,
                                    Language,
                                    Field, 
                                    Publisher, 
                                    Publication_date,
                                    Edition,
                                    Available) 
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        values = (lib_book.name, 
                  lib_book.author, 
                  lib_book.language, 
                  lib_book.field, 
                  lib_book.publisher, 
                  lib_book.pub_date, 
                  lib_book.edition, 
                  lib_book.available)
        mycursor.execute(query, values)
        cnx.commit()
        mycursor.close()

    # Add users to User table
    def add_user(self, fname, lname, email, phone):
        mycursor = cnx.cursor()
        lib_user = User(fname, lname, email, phone)
        query = "INSERT INTO User (Firstname, Lastname, Email, Phone) VALUES (%s,%s,%s,%s)"
        values = (lib_user.fname, lib_user.lname, lib_user.email, lib_user.phone)
        mycursor.execute(query, values)
        cnx.commit()
        mycursor.close()
           
    # Diplay all book in the library
    def display(self):
        mycursor = cnx.cursor()
        query = "SELECT * FROM Book"
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()

        if result:
          print("List of books:")
          for row in result:
              print(f"ID: {row[0]},\n Name: {row[1]},\n Author: {row[2]}, \n Language: {row[3]},\
                    \n Field: {row[4]},\n Publisher: {row[5]},\n Publication date: {row[6]},\
                    \n Edition: {row[7]},\n Available: {row[8]}")
        else:
            print("No books found.")

    # Edit book informations by id
    def edit(self, id):
            mycursor = cnx.cursor()
            query = "SELECT * FROM Book WHERE Book_id = %s"
            values=(id,)
            mycursor.execute(query,values)
            result = mycursor.fetchall()
          
            if result:
                while True:
                    info = input("Which one do you edit? (name,author,language,field,publisher,pub_date,edition) or exit: ")
                    info = info.lower()
                    if info == 'name':
                        new_name = input("Enter the new name: ").title()
                        query = """UPDATE Book SET name = %s
                            WHERE BOOK_id = %s"""
                        values = (new_name, id)
                        mycursor.execute(query,values)
                        cnx.commit()
                    elif info == 'author':
                        new_author = input("Enter the new author: ").title()
                        query = "UPDATE Book SET author = %s WHERE BOOK_id = %s"
                        values = (new_author, id)
                        mycursor.execute(query, values)
                        cnx.commit()
                    elif info == 'language':
                        new_language = input("Enter the new language: ").title()
                        query = "UPDATE Book SET language = %s WHERE BOOK_id = %s"
                        values = (new_language, id)
                        mycursor.execute(query, values)
                        cnx.commit()
                    elif info == 'field':
                        new_field = input("Enter the new field: ").title()
                        query = "UPDATE Book SET field = %s WHERE BOOK_id = %s"
                        values = (new_field, id)
                        mycursor.execute(query, values)
                        cnx.commit()
                    elif info == 'publisher':
                        new_publisher = input("Enter the new publisher: ").title()
                        query = "UPDATE Book SET publisher = %s WHERE BOOK_id = %s"
                        values = (new_publisher, id)
                        mycursor.execute(query, values)
                        cnx.commit()
                    elif info == 'pub_date':
                        new_pub_date = input("Enter the new publication date: ")
                        query = "UPDATE Book SET publication_date = %s WHERE BOOK_id = %s"
                        values = (new_pub_date, id)
                        mycursor.execute(query, values)
                        cnx.commit()
                    elif info == 'edition':
                        new_edition = input("Enter the new edition: ")
                        query = "UPDATE Book SET edition = %s WHERE BOOK_id = %s"
                        values = (new_edition, id)
                        mycursor.execute(query, values)
                        cnx.commit()
                    elif info == "":
                        pass
                    elif info =="exit":
                        break
                    else:
                        print("Invalid input. Please try again.")
                   
            else:
                print("Book not found") 
            mycursor.close()          
    
    # Remove book from Book table by id number
    def remove(self, id): 
        mycursor = cnx.cursor()
        query = "DELETE FROM Book WHERE BOOK_id = %s"
        values = (id, )
        mycursor.execute(query, values)
        cnx.commit()
        mycursor.close()                   

    # Search book by name
    def search(self, name):
        mycursor = cnx.cursor()
        query = "SELECT * FROM Book WHERE name LIKE %s"
        name = "%" + name + "%"
        values = (name,)
        mycursor.execute(query, values)
        result = mycursor.fetchall()
        mycursor.close()
        return result
         
     
    # Borrow book
    def borrow_book(self, id_book, id_user, name):
        mycursor = cnx.cursor()
        dborrow = datetime.now()
        dreturn = datetime.now() + timedelta(days=10)
        
        # Check if book is available
        check_query = "SELECT Available FROM Book WHERE Book_id = %s"
        check_values = (id_book, )
        mycursor.execute(check_query, check_values)
        result = mycursor.fetchone()
        if result is None:
            print("Book not found")
            return
        available = result[0]
        if available != 'True':
            print("Book is not available")
            return
        
        # Update book availability
        update_query = "UPDATE Book SET Available = 'False' WHERE Book_id = %s"
        update_values = (id_book, )
        mycursor.execute(update_query, update_values)
        
        # Insert borrow record
        insert_query = """INSERT INTO Borrow 
                        (ID_book, ID_user, Name_book, Date_borrow, Date_return) 
                        VALUES (%s, %s, %s, %s, %s)"""
        insert_values = (id_book, id_user, name, dborrow, dreturn)
        mycursor.execute(insert_query, insert_values)
        
        cnx.commit()
        mycursor.close()

    # Return book
    def return_book(self, id, book_id):
        mycursor = cnx.cursor()

        # Update book availability
        update_query = "UPDATE Book SET Available = 'True' WHERE Book_id = %s"
        update_values = (book_id, )
        mycursor.execute(update_query, update_values)
        
        # Delete borrow record
        delete_query = "DELETE FROM Borrow WHERE ID = %s"
        delete_values = (id, )
        mycursor.execute(delete_query, delete_values)

        cnx.commit()
        mycursor.close()


