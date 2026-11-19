from Employee import Employee
from PermanentEmployee import PermanentEmployee
from ContractEmployee import ContractEmployee

Permanent = PermanentEmployee('Akash','IT',60000)
Permanent.display_details()
Permanent.calculate_salary()

Contract = ContractEmployee('Ramanan' , 'IT', 40000)
Contract.display_details()
Contract.calculate_salary()
       