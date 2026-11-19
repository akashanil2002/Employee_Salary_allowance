from Employee import Employee

class ContractEmployee(Employee):
         def calculate_salary(self):
            allowance = self.salary * 0.05
            total = self.salary + allowance
            print('The ContractEmployee Salary -', total)
            return total