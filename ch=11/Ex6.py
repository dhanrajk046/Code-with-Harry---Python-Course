class Employee:
    a=None
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
            return f"{self.fname}{self.lname}"
        
    @name.setter
    def name(self,value):
         self.fname=value.split(" ")[0]
         self.lname=value.split(" ")[1]


e=Employee()
Employee.a=45
e.name="Harry Khan"
print(e.fname,e.lname)
e.show()


# class Employee:
#     a = None   # define at class level

#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name(self, value):
#         self.fname, self.lname = value.split(" ")

# e = Employee()
# Employee.a = 45   # set class attribute
# e.name = "Harry Khan"
# print(e.fname, e.lname)   # Harry Khan
# e.show()                  # The class attribute of a is 45