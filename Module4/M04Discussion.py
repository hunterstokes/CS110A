# Question 2: Error Hunt B

# Is each piece of code valid? If so specify the output. If not: Identify the type of error. Describe IN YOUR OWN WORDS the error. Show the correct code.

# Code A:

language = 'Python'
year = 2022
print('learn', language, 'in', year)

# EXPECTED OUTPUT: learn Python in 2022

# Code B:

person = 'child'
age = '10'
next_age = age + 1
print('the', person, 'is', age, 'but will be', next_age, 'soon')

# EXPECTED OUTPUT: the child is 10 but will be 11 soon
# This code does not run, the value of 1 cannot be added to a string
# to fix this we would need to change the value of age to an integer:
 age = 10

# Code C:

first_name = 'rudy'
last_name = 'day'
print('hello first_name last_name')

# EXPECTED OUTPUT: hello rudy day
# This code does not run, the variables first_name and last_name are not being called correctly, they are instead being put inside of the string. To fix this we need to put the variables outside of the string.
    print('hello', first_name, last_name)

# Code D:

sub_total = 100
tax = 9.95
total = sub_total + tax
print('the total is', total, '\npay up!')

