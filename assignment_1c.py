#Phelopatir Beshay
#Assignment 1c

#Part 1
name_of_object = input("Enter the name of the object: ")
mass_kg = input("What is the mass of the object in kg? ")
velocity = input("What is the velocity of the object in m/s? ")
#Gathers input

name_of_object_clean = name_of_object.strip().title()
mass_kg_num = float(mass_kg)
velocity_num = float(velocity)
#Makes input usable

#Part 2
KE_joules = 0.5*mass_kg_num*(velocity_num**2)
#Runs equation for joules using cleaned up numbers

KE_calories = KE_joules/4.184
KE_ergs = KE_joules * 10**7
#Converts joules to calories and ergs respectively

#Part 3
output_line_one = f"Kinetic Energy Report for: {name_of_object_clean}"
output_line_two = "----------------------------"
output_line_three = f"Joules:\t{KE_joules} J\nCalories:\t{KE_calories} cal\nErgs:\t{KE_ergs} erg"
#Variables for the report
print(output_line_one)
print(output_line_two)
print(output_line_three)
#Prints the report in order