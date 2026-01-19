except ValueError as v:
    print("Heyyyyy")
    print(v)


# import random

# n = random.randint(1, 100)
# guesses = 1
# a = -1

# while a != n:
#     try:
#         a = int(input("Guess the number: "))

#         if a > n:
#             print("Lower number please")
#             guesses += 1
#         elif a < n:
#             print("Higher number please")
#             guesses += 1

#     except ValueError as v:
#         print("Heyyyyy")
#         print(v)
#         print("Please enter a valid number!")

# print(f"You have guessed the number {n} correctly in {guesses} attempts")
