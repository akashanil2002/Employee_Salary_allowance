# Import ABC and abstractmethod from the abc module
from abc import ABC , abstractmethod


# Create an abstract class called Employee
class Employee(ABC):
    def __init__(self,employee_name, department , salary):  # Constructor: Initialises employee details
        self.employee_name = employee_name  # Store employee name
        self.department = department  # Store employee department
        self.__salary = salary   # Private variable to store salary (Encapsulation)

# Property allows salary to be accessed 
    @property

    def salary(self):
        return self.__salary

# Method to display employee information
    def display_details(self):
        print('Name :' , self.employee_name)  # Display employee name
        print('Department :' , self.department) # Display employee department
        print('Salary :' , self.salary)   # Display employee salary using the property
       
# Abstract method: Must be implemented by child classes
    @abstractmethod
    def calculate_salary(self):
        pass