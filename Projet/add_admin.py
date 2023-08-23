from utils import cnx
from admin import *


# Add Admin to Database
def add_admin(fname, lname, username, password):
        try:
            mycursor = cnx.cursor()
            lib_admin = Admin(fname, lname, username, password)
            # Query the admin table for existing records with the same username and password combination
            mycursor = cnx.cursor()
            mycursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
            result = mycursor.fetchall()

            # Check if any records were returned
            if len(result) > 0:
            # A record with the same username and password combination already exists
                print("Username and password combination already exists")
                
            else:
            # No record with the same username and password combination was found, it is unique
            # Create the new admin account with the provided username and password
                query = "INSERT INTO Admin (Firstname,Lastname,Username, Password) VALUES (%s,%s,%s,%s)"
                values = (lib_admin.fname, lib_admin.lname, lib_admin.username, lib_admin.password)
                mycursor.execute(query, values)
                cnx.commit()
                mycursor.close()
                print("Admin added successfully")
        except:
            print("Failed to add admin")


while True:
    fname = input('Firstname: ').title()
    lname = input('Lastname: ').title()
    username = input('Username: ')
    password = input('password: ')
    add_admin(fname, lname, username, password)
    answer = input('If you are an user, Do you want to try again? (y/n)').lower()
    if answer == 'y':
            continue
    else:
        print('Goodbye!')
        break