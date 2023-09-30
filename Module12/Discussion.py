# Part A:
# There are three things wrong with this program.

# List each problem by line number and explain the problem IN YOUR OWN words
# Fix all problems, showing correct code

# print("This program takes three numbers and returns the sum.")
# total = 0 # Total starts at value 0
# for i in range(3): # For loop from 0 to 2
#     x = int(input("Enter a number: ")) # User input, we must make sure it is defined as an integer and not a string.
#     total += x  # Total is equal to total plus i, but x is ignored, x must be put in the statement
# print("The total is:", total) # Asking to print x would not work, since x is not defined outside of the loop. Therefore, we must swap it with x. 

# Write a for loop to print your name 10 times, and then the word ``Done'' at the end.

for i in range(10):
    print("Hunter Brown")
print("Done")