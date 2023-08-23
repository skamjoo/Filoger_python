from person import *


class Admin(Person):
    def __init__(self, fname, lname, username, password):
        super().__init__(fname,lname)
        self.username = username
        self.password = password

    def all_info(self):
        print(f"The unique id of admin is : {self.unique_id}")
        print(f"The  first name of admin is: {self.fname}")
        print(f"The last name of admin  is: {self.lname}")
        print(f"The user_name of admin  is: {self.username}")   
        print(f"The password of admin is: {self.password}")
        print("+"*50)





    