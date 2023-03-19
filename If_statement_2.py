#!/usr/bin/python3
# Read the month name from the user
month_name = input("Enter the name of a month: ")

# Compute the number of days in the month
if month_name == "February":
    days = "28 or 29"
elif month_name in ("April", "June", "September", "November"):
    days = 30
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    days = 31
else:
    print("Please enter a valid month name.")
    days = None

# Display the result
if days is not None:
    print("The month of", month_name, "has", days, "days in it.")

    
    
