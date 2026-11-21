# Import the Employee parent class from Employee.py
from Employee import Employee

# Create a child class called PermanentEmployee
# It inherits the properties and methods of Employee
class PermanentEmployee(Employee):
    def calculate_salary(self):    # Implement the abstract method from the parent class
            allowance = self.salary * 0.20  # Calculate 20% allowance based on basic salary
            total = self.salary +  allowance  # Add the allowance to the basic salary
            print('The permentEmployee Salary -', total) # Display the permanent employee's total salary
            return total  # Return the calculated total salary