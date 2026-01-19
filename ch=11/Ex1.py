class Employee:
    company="ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} ")

class Programmer(Employee):
    company="ITC INFOTECH"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a=Employee()
b=Programmer()
print(a.company,b.company)