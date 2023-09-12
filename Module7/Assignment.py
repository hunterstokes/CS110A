# UPDATE: Birthday Printer
# Author: Hunter Brown
# Date: 09/11/2023


# Ask for and read in the user's name
user_name = input("What is your name? ")
print("Hello, " + user_name + ".")
# Ask for and read in the user's age
user_age = int(input("What is your age? "))
# Print a message to the user that contains their future age.
# Calculate how old the user will be after their next birthday
user_age_next_birthday = user_age + 1
print("You will be " + str(user_age_next_birthday) + " on your next birthday.")
# Ask for and read in the user's month 
user_month = input("What month were you born in? ")
# Ask for and read in the user's date
user_date = int(input("What date were you born on? "))
# Ask for and read in the user's year 
user_year = int(input("What year were you born in? "))
# Ask for and read in the user's day of the week of their birthday
user_day_of_week = input("What day of the week were you born on? ")
# Output the birthday in the U.S. format
print("In the U.S it would read: " + user_month + " " + str(user_date) + ", " + str(user_year) + " on a " + user_day_of_week + ".")
# Output the birthday in the European format
print("In Europe it reads: " + user_day_of_week + " " + str(user_date) + " " + user_month + " " + str(user_year) + ".")

# Sample Output:
"""What is your name? hunt
Hello, hunt.
What is your age? 12
You will be 13 on your next birthday.
What month were you born in? 25
What date were you born on? 22
What year were you born in? 1234
What day of the week were you born on? tues
In the U.S it would read: 25 22, 1234 on a tues.
In Europe it reads: tues 22 25 1234."""

"""What is your name? Hunter
Hello, Hunter.
What is your age? 33
You will be 34 on your next birthday.
What month were you born in? December
What date were you born on? 03
What year were you born in? 1995
What day of the week were you born on? Monday
In the U.S it would read: December 3, 1995 on a Monday.
In Europe it reads: Monday 3 December 1995."""
