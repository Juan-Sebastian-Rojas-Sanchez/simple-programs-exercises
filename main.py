#pitagoras
import math

# Get input from the user
a = float(input("Enter leg a: "))
b = float(input("Enter leg b: "))

# Calculate the length of the hypotenuse
c = math.sqrt(a**2 + b**2)

# Print the result
print(f"The hypotenuse is {c}.")