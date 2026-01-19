class Employee:
    Language = "Python"
    salary = 1200000
    # This is a class attribute

    def getInfo(self):
        print(f"The language is {self.Language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry=Employee()
#harry.Language="Javascript"
#This is an instance attribute
harry.greet()
harry.getInfo()
#Employee.getInfo(harry)

