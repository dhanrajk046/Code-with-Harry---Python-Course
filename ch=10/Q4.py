class Calculator:
    def __init__(self, number):
        self.number = number
    
    def square(self):
        print(f"The square of {self.number} is {self.number ** 2}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number ** 3}")
    def squareroot(self):
        print(f"The square root of {self.number} is {self.number ** 0.5}")  

    @staticmethod
    def hello():
        print("Hello! There")  

a=Calculator(4) 
a.hello() 
a.square()
a.cube()
a.squareroot()
