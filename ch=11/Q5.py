class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # Dot product
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print("v1 + v2 =", v1 + v2)   # Vector addition
print("v1 * v2 =", v1 * v2)   # Dot product
print("v1 + v3 =", v1 + v3)   # Vector addition
print(v1+v3)