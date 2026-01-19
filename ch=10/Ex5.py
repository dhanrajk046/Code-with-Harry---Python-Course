class Employee:
    language="Python"
    salary=1200000

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
harry=Employee()
harry.language="JavaScript"
harry.getInfo()