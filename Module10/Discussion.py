# While Loops Part 1

# Question 1: Write a while loop in Python that lets the user enter a number. The number should be multiplied by 10, and the result stored (assigned) in the variable named product.  The loop should iterate as long as product contains a value less than 100.

product = int(input())

while product < 100:
    product = product * 10
    print(product)

# This code contains ERRORS in the loop
count = 1
total = 0
while (count <= 10:)
    total = total + count;
print("The sum of the numbers 1-10 is : ")
print(total)

# The error is here: while (count <= 10:)
# To fix this we need to move the colon outside of the parentheses

while (count <= 10):
    total = total + count


