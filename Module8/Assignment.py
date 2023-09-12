# This is the Magic date finder program.

# Ask user to input a day, month, and year.
day = int(input("Enter a day: XX"))
month = int(input("Enter a month: XX"))
year = int(input("Enter a two digit year: XX"))

if day * month == year:
    print("This is a magic date!")
else:
    print("This is not a magic date.")
