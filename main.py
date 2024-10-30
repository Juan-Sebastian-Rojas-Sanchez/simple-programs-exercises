#Que nota nesecito
# Get input from the user
C1 = float(input("Enter grade for exam 1: "))
C2 = float(input("Enter grade for exam 2: "))
NL = float(input("Enter lab grade: "))

# Desired final grade
desired_final_grade = 60

# Calculate the required grade for the third exam
# Using the formula NF = NC * 0.7 + NL * 0.3
# We can derive NC = (desired_final_grade - NL * 0.3) / 0.7
NC_required = (desired_final_grade - NL * 0.3) / 0.7

# Calculate the required grade for the third exam
C3_required = NC_required * 3 - (C1 + C2)

# Print the required grade for the third exam
print(f"You need a grade of {C3_required:.2f} in exam 3.")