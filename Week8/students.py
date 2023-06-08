class Student:
    def __init__(self,s_number,f_name,_l_name,age,grade):
        self.student_number=s_number
        self.first_name=f_name
        self.last_name=_l_name
        self.age=age
        self.grade=grade
        
    def get_name(self):
        # print(f"name of student: {self.first_name}")   
        return self.first_name
    
    def get_all_info(self):
        print(f"The number_student  is: {self.student_number}")
        print(f"The first_name  is: {self.first_name.title()}")
        print(f"The last_name  is: {self.last_name.title()}")   
        print(f"The age  is: {self.age}")
        print(f"The grade are : {self.grade}")
        print("-"*50)  
    