#defining the function to check the divisibility using modulus operator
def checkDivisibility(n):
    if n % 7 == 0:
        print(n, "is divisible by 7")
    else:
        print(n, "is not divisible by 7")

#asking user to provide value for a number
n = int(input("Enter a number to check if it is divisible by 7 : "))

#calling the function
checkDivisibility(n)
