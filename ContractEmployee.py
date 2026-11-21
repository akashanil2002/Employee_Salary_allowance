# Import the Employee parent class from Employee.py
from Employee import Employee


# Create a child class called ContractEmployee
# It inherits attributes and methods from the Employee class
class ContractEmployee(Employee):
         def calculate_salary(self):  # Implement the abstract method from the parent class
            allowance = self.salary * 0.05 # Calculate 5% allowance based on the basic salary
            total = self.salary + allowance # Add the allowance to the basic salary
            print('The ContractEmployee Salary -', total) # Display the contract employee's total salary
            return total # Return the calculated total salary