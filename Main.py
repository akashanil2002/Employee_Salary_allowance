# Import the parent Employee class
from Employee import Employee
# Import the PermanentEmployee child class
from PermanentEmployee import PermanentEmployee
# Import the ContractEmployee child class
from ContractEmployee import ContractEmployee

# Create an object of PermanentEmployee class
# Arguments: employee_name, department, basic_salary
Permanent = PermanentEmployee('Akash','IT',60000)
Permanent.display_details() # Display the permanent employee's details
Permanent.calculate_salary() # Calculate and display the permanent employee's total salary


# Create an object of ContractEmployee class
# Arguments: employee_name, department, basic_salary
Contract = ContractEmployee('Ramanan' , 'IT', 40000) 
Contract.display_details() # Display the contract employee's details
Contract.calculate_salary() # Calculate and display the contract employee's total salary


#Output
# Name : Akash
# Department : IT
# Salary : 60000
# The permentEmployee Salary - 72000.0
# Name : Ramanan
# Department : IT
# Salary : 40000
# The ContractEmployee Salary - 42000.0