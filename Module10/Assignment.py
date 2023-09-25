# UPDATE: Butterfly Tracker
# Author: Hunter Brown
# Date: 09/16/2023

# This is a program to track the number of butterflies caught.

# Initialize variables
# Start with no butterflies and no total
butterfly = 0
total = 0
# Print statement to introduce the program
print("Enter the number of butterflies you have collected for each day you spent in the field. Please enter -1 when finished.")

# This statement is technically uneeded, but it is here to make the program more user friendly.
butterfly = int((input("Enter the number of butterflies you caught today(-1 to quit):  ")))

# while the user enters positive values, add them to the total
while butterfly >= 0:
    # Gets the user input for the number of butterflies caught
    # This comes first to ensure even if the user input is not -1 and it is a different negative value, it will not take away from the totatl.
    total = total + butterfly
    # Total the butterflies caught
    butterfly = int(input("Enter the number of butterflies you caught today(-1 to quit):  "))
 
# Final print statement once the user is done entering butterflies
print("You have caught",total,"butterflies.")

""""
➜  Module10 git:(main) ✗ python3 Assignment.py
Enter the number of butterflies you have collected for each day you spent in the field. Please enter -1 when finished.
Enter the number of butterflies you caught today(-1 to quit):  1
Enter the number of butterflies you caught today(-1 to quit):  2
Enter the number of butterflies you caught today(-1 to quit):  3
Enter the number of butterflies you caught today(-1 to quit):  4
Enter the number of butterflies you caught today(-1 to quit):  5
Enter the number of butterflies you caught today(-1 to quit):  -1
You have caught 15 butterflies.
➜  Module10 git:(main) ✗ 
Enter the number of butterflies you have collected for each day you spent in the field. Please enter -1 when finished.
Enter the number of butterflies you caught today(-1 to quit):  12345678
Enter the number of butterflies you caught today(-1 to quit):  word
Traceback (most recent call last):
  File "/Users/hunterbrown/School/CS110A/Module10/Assignment.py", line 16, in <module>
    butterfly = int(input("Enter the number of butterflies you caught today(-1 to quit):  "))
ValueError: invalid literal for int() with base 10: 'word'
➜  Module10 git:(main) ✗ 

➜  Module10 git:(main) ✗ python3 Assignment.py
Enter the number of butterflies you have collected for each day you spent in the field. Please enter -1 when finished.
Enter the number of butterflies you caught today(-1 to quit):  27
Enter the number of butterflies you caught today(-1 to quit):  32
Enter the number of butterflies you caught today(-1 to quit):  88
Enter the number of butterflies you caught today(-1 to quit):  -47
You have caught 147 butterflies.

➜  Module10 git:(main) ✗ python3 Assignment.py
Enter the number of butterflies you have collected for each day you spent in the field. Please enter -1 when finished.
Enter the number of butterflies you caught today(-1 to quit):  7
Enter the number of butterflies you caught today(-1 to quit):  8
Enter the number of butterflies you caught today(-1 to quit):  9
Enter the number of butterflies you caught today(-1 to quit):  27
Enter the number of butterflies you caught today(-1 to quit):  42
Enter the number of butterflies you caught today(-1 to quit):  -3
You have caught 93 butterflies.
➜  Module10 git:(main) ✗ 
"""