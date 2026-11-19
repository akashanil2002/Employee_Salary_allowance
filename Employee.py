from abc import ABC , abstractmethod



class Employee(ABC):
    def __init__(self,employee_name, department , salary):
        self.employee_name = employee_name
        self.department = department
        self.__salary = salary


    @property

    def salary(self):
        return self.__salary

    def display_details(self):
        print('Nme :' , self.employee_name)
        print('Department :' , self.department)
        print('Salary :' , self.salary)
       

    @abstractmethod
    def calculate_salary(self):
        pass