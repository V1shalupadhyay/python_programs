sum = 0
#Getting the number input from user
n = int(input("Enter the number: "))
for a in range(1,n+1):
    #calculating the sum
    sum = sum + (1/pow(a,3))
#Sum of the series is
print("The sum of the series is: ",round(sum,2))
