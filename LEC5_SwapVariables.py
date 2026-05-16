# =========================================
# LEC 5 - Swap Variables
# Student Name: Awais Farooq
# =========================================

# Taking User Input
a = input("Enter first value: ")
b = input("Enter second value: ")

print("\nBefore Swapping")
print("First Value:", a)
print("Second Value:", b)

# Swapping without third variable
a, b = b, a

print("\nAfter Swapping")
print("First Value:", a)
print("Second Value:", b)