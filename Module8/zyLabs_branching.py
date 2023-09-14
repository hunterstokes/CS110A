# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

# Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.


highway_number = int(input())

if highway_number <= 0:
    print(highway_number,"is not a valid interstate highway number.")
elif highway_number % 2 == 0 and highway_number < 100:
    print(f'I-{highway_number} is primary, going east/west.')
elif highway_number % 2 == 1 and highway_number < 100:
    print(f'I-{highway_number} is primary, going north/south.')
elif highway_number % 100 == 0:
    print(highway_number,"is not a valid interstate highway number.")
elif highway_number % 2 == 0 and highway_number <= 999:
    print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going east/west.')
elif highway_number % 2 == 1 and highway_number <= 999:
    print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going north/south.')
else:
    print(highway_number,"is not a valid interstate highway number.")

