#Program to find sum of digits of an integer number
#Initializing the sum to zero
sum = 0
#Getting user input
n = float(int(input("Enter the number: ")))
# looping through each digit of the number
# Modulo by 10 will give the first digit and
# floor operator decreases the digit 1 by 1
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n//10
# Printing the sum
print("The sum of digits of the number is",sum)
