from Employee import Employee

class PermanentEmployee(Employee):
    def calculate_salary(self):
            allowance = self.salary * 0.20
            total = self.salary +  allowance
            print('The permentEmployee Salary -', total)
            return total