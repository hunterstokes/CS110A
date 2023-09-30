# UPDATE: Temperature Converter
# Author: Hunter Brown
# Date: 09/29/2023

# This is a program to convert Celsius to Fahrenheit.
# Setting up print statements to align the table
print('Celsius     Fahrenheit')
print('------------------')
# Initialize variables
Celsius = -8
# Initialize variables
for Celsius in range(-8, 11, 2):
    # Calculate Fahrenheit
    Fahrenheit = (9/5) * Celsius + 32
    # Print the table
    print(f"{Celsius}     \t     {Fahrenheit}")\



"""SAMPLE OUTPUT:
➜  module12 git:(main) ✗ python3 Assignment.py
Celsius     Fahrenheit
------------------
-8           17.6
-6           21.2
-4           24.8
-2           28.4
0            32.0
2            35.6
4            39.2
6            42.8
8            46.4
10           50.0
➜  module12 git:(main) ✗ python3 Assignment.py
Celsius     Fahrenheit
------------------
-8           17.6
-6           21.2
-4           24.8
-2           28.4
0            32.0
2            35.6
4            39.2
6            42.8
8            46.4
10           50.0
➜  module12 git:(main) ✗ python3 Assignment.py
Celsius     Fahrenheit
------------------
-8           17.6
-6           21.2
-4           24.8
-2           28.4
0            32.0
2            35.6
4            39.2
6            42.8
8            46.4
10           50.0
➜  module12 git:(main) ✗ 


"""