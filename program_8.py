# 🔍 Comparison Operators

#Compare three numbers and print the greatest one using comparison operators.

num1 = int(input("Enter the number 1 = "))
num2 = int(input("enter the number 2 = "))
num3 = int(input("Enter the number 3 = "))

if num1 >= num2 and num1 >= num3:
    print("Number 1 is the greatest")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is the greatest")
else:
    print("Number 3 is the greatest")
