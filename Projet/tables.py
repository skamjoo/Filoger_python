from config_func import cnx

mycursor = cnx.cursor()

# Table of books
tab_book = """ CREATE TABLE Book(
                Book_id INT NOT NULL auto_increment,
                Name  varchar(255) NOT NULL,
                Author varchar(255) NOT NULL,
                Language varchar(255),
                Field varchar(255) NOT NULL,
                Publisher varchar(255),
                Publication_date varchar(255),
                Edition varchar(50) NOT NULL,
                Available varchar(50) NOT NULL,
                PRIMARY KEY (book_id)
                );
            """
try:
    mycursor.execute(tab_book)
except:
    print('BOOK table exists')

# Tables of users
tab_user = """ CREATE TABLE User(
                User_id INT NOT NULL auto_increment,
                Firstname  varchar(255),
                Lastname varchar(255) NOT NULL,
                Email varchar(255) NOT NULL,
                Phone varchar(255) NOT NULL,
                PRIMARY KEY (User_id)
                );
            """
try:
    mycursor.execute(tab_user)
except:
    print('USER table exists')

# Table of admin
tab_admin = """ CREATE TABLE Admin(
                 Admin_id INT NOT NULL auto_increment,
                 Firstname  varchar(255),
                 Lastname varchar(255) NOT NULL,
                 Username varchar(255) NOT NULL,
                 Password varchar(255) NOT NULL,
                 PRIMARY KEY (admin_id)
                );
            """
try:
    mycursor.execute(tab_admin)
except:
    print('ADMIN table exists')

# Table of borrow
tab_borrow = """ CREATE TABLE Borrow(
                  ID INT NOT NULL auto_increment,
                  ID_book int NOT NULL,
                  Name_book varchar(255) NOT NULL,
                  Date_borrow varchar(255) NOT NULL,
                  Date_return varchar(255) NOT NULL,
                  ID_user int NOT NULL,
                  PRIMARY KEY (ID),
                  FOREIGN KEY (ID_book) REFERENCES Book (Book_id),
                  FOREIGN KEY (ID_user) REFERENCES User (User_id)
                  );
             """
try:
    mycursor.execute(tab_borrow)
except:
    print('BORROW table exists')



