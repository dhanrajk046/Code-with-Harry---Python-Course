class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The vector is {self.i}i+{self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k
        
        
    def show(self):
        print(f"The vector is {self.i}i+{self.j}j+{self.k}k")


a=TwoDVector(1,2)
a.show()
b=ThreeDVector(1,2,3)
b.show()

# class TwoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")


# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)   # initialize i and j from parent
#         self.k = k              # add k for 3D vector

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# # Usage
# a = TwoDVector(1, 2)
# a.show()   # The vector is 1i + 2j

# b = ThreeDVector(3, 4, 5)
# b.show()   # The vector is 3i + 4j + 5k