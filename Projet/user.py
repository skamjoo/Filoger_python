from person import *

class User(Person):
    def __init__(self, fname, lname, email, phone):
        super().__init__(fname,lname)
        self.email = email
        self.phone = phone
        self.email = email
        self.phone = phone

    def user_info(self):
        print(f"The unique id of user is : {self.unique_id}")
        print(f"The  first name of user is: {self.fname}")
        print(f"The last name of user  is: {self.lname}")
        print(f"The eamil of user  is: {self.email}")   
        print(f"The phone number of user  is: {self.phone}")
        print("+"*50)

