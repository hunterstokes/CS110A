# UPDATE: Magic Dates
# Author: Hunter Brown
# Date: 09/16/2023

# This is a program to see if the user-inputted date is a magic date.
# A magic date is when the month times the day is equal to the year.
# Intro to the program describing to the user how it should work.
print("Welcome to the magic date program.")
print("This program will tell you if the date you input is a magic date.")
print("A magic date is when the month times the day is equal to the year.")
print("Please only use numerical values for the month, day, and year.")
# Give the user a prompt to start the program when they are ready.
print("Press 'enter' key to begin.")
start = input()
# Ask user to input a day, month, and year.
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a two digit year: "))

if day * month == year:
    print("This is a magic date!")
else:
    print("This is not a magic date.")


# enter a month (in numeric form)
# enter a day
# enter a two-digit year
# if the month times the day is equal to the year
# then
#     display a message saying the date is magic
# else
#     display a message saying the date is not magic

"""Module8 git:(main) ✗ python3 Assignment.py
Welcome to the magic date program.
This program will tell you if the date you input is a magic date.
A magic date is when the month times the day is equal to the year.
Please only use numerical values for the month, day, and year.
Press 'enter' key to begin.

Enter a month: 5
Enter a day: 4
Enter a two digit year: ab
Traceback (most recent call last):
  File "~/CS110A/Module8/Assignment.py", line 18, in <module>
    year = int(input("Enter a two digit year: "))
ValueError: invalid literal for int() with base 10: 'ab'
➜  Module8 git:(main) ✗  
------------------------------------------------------------------------
➜  Module8 git:(main) ✗ python3 Assignment.py
Welcome to the magic date program.
This program will tell you if the date you input is a magic date.
A magic date is when the month times the day is equal to the year.
Please only use numerical values for the month, day, and year.
Press any button and then the 'enter' key to continue.

Enter a month: 12
Enter a day: 03
Enter a two digit year: 36
This is a magic date!
------------------------------------------------------------------------
➜  Module8 git:(main) ✗ python3 Assignment.py
Welcome to the magic date program.
This program will tell you if the date you input is a magic date.
A magic date is when the month times the day is equal to the year.
Please only use numerical values for the month, day, and year.
Press 'enter' key to begin.

Enter a month: 12
Enter a day: 03
Enter a two digit year: 95
This is not a magic date.
➜  Module8 git:(main) ✗ 

"""