
from students import *
class School:
    def __init__(self,m_students):
        self.students = []
        self.max_students = m_students

    def find_index(self,id_number) :
        for i,item in enumerate(self.students):
            if item.student_number == id_number:
                return i
        return -1

    def add_student(self,student):
        index = self.find_index(student.student_number)
        if index == -1:
            if len(self.students) < self.max_students:
                self.students.append(student)
                print("added to the class")
            else:
                print("Sorry, the class is full.")    
        else:
            print(f"student with  number student ={student.student_number} exist")    

    def display(self):
        l = len(self.students)
        if l == 0:
            print("Empty")
            return
        for s in self.students:
            s.get_all_info()   

    def search(self,name):
        found_students = []
        for s in self.students:
            if s.get_name() == name:
                found_students.append(s)
        if len(found_students) == 0:
            print(f"No students with name {name.title()} found in the class.")
        else:
            print(f"{len(found_students)} students with name '{name.title()}' were found.")
            print('+'*40)
            for fs in found_students:
                fs.get_all_info()   
        return found_students
        
    def edit(self,id_number):
          index = self.find_index(id_number)     
          if index != -1:
            new_info = input("Firstname, Lastname, Age, and Scores: ")
            info = new_info.split(",")
            self.students[index].first_name = info[0] or self.students[index].first_name
            self.students[index].last_name = info[1] or self.students[index].last_name
            self.students[index].age = info[2] or  self.students[index].age
            self.students[index].grade = info[3] or  self.students[index].grade
            #self.students[index].scores=self.students[index].scores.split()
            print("Edited")    
          else:
             print("NOT found!")  

    def remove(self,id_number): 
        index = self.find_index(id_number) 
        if index != -1:
             self.students.pop(index)
             print("Removed")
        else:
             print("NOT found")
                     