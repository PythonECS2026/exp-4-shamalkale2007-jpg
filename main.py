#Aim: Calculating simple interest
#Coder: Shamal
#Date:26/01/26
#Class:ECS/E2

print("simple interest calculator")
principal=float(input("Enter the principal amount:"))
Rate=float(input("Enter the rate of interest:"))
Time=float(input("Enter the time period(in years):"))
SimpleInterest=(principal*Rate*Time)/100
print("Simple Interest:", SimpleInterest)
