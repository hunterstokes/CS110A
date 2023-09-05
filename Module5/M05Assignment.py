# This program calculates butterfly population estimates
# Modified by:  Hunter Brown
# Modified Date: 09/04/2023

print("Butterfly Estimator\n")
# input/get data
males = int(input("Enter the estimated males population: "))
females = int(input("Enter the estimated females population: "))

# perform calculations
total_butterflies = males + females
sex_ratio = males // females
ratio_variance = males % females
gender_difference = males - females
mating_pairs = males * females

# output results
print("\nTotal Butterflies: " , total_butterflies)
print("Sex Ratio          : " , sex_ratio)
print("Variance           : " , ratio_variance)
print("Gender Difference  : " , gender_difference)
print("Mating Pairs       : " , mating_pairs)

# SAMPLE OUTPUT: 
"""
Butterfly Estimator

Enter the estimated males population: 80
Enter the estimated females population: 30

Total Butterflies:  110
Sex Ratio          :  2
Variance           :  20
Gender Difference  :  50
Mating Pairs       :  2400
"""

"""
Butterfly Estimator

Enter the estimated males population: 100
Enter the estimated females population: 0
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    sex_ratio = males // females
ZeroDivisionError: integer division or modulo by zero
"""