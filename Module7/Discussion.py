# When I run this code:

message ='Year is '
year = 2018
#print(message + year) 
# I get this output:

# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     print(message + year)
# TypeError: can only concatenate str (not "int") to str

# Explain why and show at least 2 ways to fix the print ( you may show more than 2 if you want):

#print(message + year) #fix me
print(message + str(year)) 
print(message, year)
print(message, str(year))