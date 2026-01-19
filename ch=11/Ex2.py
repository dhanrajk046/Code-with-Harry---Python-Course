class Employee:
    company="ITC"
    name="Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class coder:
    language="Python"
    def printlanguage(self):
        print(f"Out of all the language here is your language {self.language}")
    
class Programmer(Employee,coder):
    company="ITC Infotech" 
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language") 

a=Employee()
b=Programmer()

b.show()
b.printlanguage()
b.showlanguage()
