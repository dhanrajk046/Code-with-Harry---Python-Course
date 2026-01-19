class Employee:
  language="Python"
  salary=1200000

  def __init__(self, name, salary, language):
    self.name=name
    self.salary=salary
    self.language=language
    print("I am creating an object")

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}.")

  @staticmethod
  def greet():
    print("Good Morning")

harry = Employee("Harry",1200000,"Javascript")
#harry.name="Harry"
print(harry.name, harry.salary, harry.language)
#rohan=Employee()
harry.getInfo()
harry.greet()