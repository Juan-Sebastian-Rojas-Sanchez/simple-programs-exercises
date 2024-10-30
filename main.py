#Hora futura
#  Get the current hour and number of hours from the user
current_hour = int(input("Current hour: "))
hours_to_add = int(input("Number of hours: "))

# Calculate the new hour
new_hour = (current_hour + hours_to_add) % 12

# Adjust for 12 o'clock case
if new_hour == 0:
    new_hour = 12

# Print the result
print(f"In {hours_to_add} hours, the clock will show {new_hour}.")