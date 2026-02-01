# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:Shamal 
# Date:26/01/26
print("Simple Interest Calculator")
principleAmount = float(input("Enter the principle amount: "))
rateOfInterest = float(input("Enter the rate of interest: "))
timePeriod = float(input("Enter the time period (in years): "))
simple_interest = (principleAmount*rateOfInterest*timePeriod)/100
print("Simple Interest:", simple_interest)
