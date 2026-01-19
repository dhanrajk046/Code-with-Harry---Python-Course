

class Vector:
    def __init__(self, values):
        self.values = values   # store the list of numbers

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return f"Vector({self.values})"


# Example usage
v1 = Vector([1, 2, 3])
print(len(v1))     # Output: 3
# print(v1)          # Output: Vector([1, 2, 3])