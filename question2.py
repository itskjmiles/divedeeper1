# Task 1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)
print("The largest number is:", largest)

# Task 2
smallest = min(num1, num2, num3)
print("The smallest number is:", smallest)

# Task 3
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("There are two numbers equal to each other.")
else:
    print("There are no equal numbers.")
