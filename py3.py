#Asking for the number of days taken by A, B, C to complete the work alone
x = int(input('Enter the number of days required by A to complete work alone: '))
y = int(input('Enter the number of days required by B to complete work alone: '))
z = int(input('Enter the number of days required by C to complete work alone: '))

#calculating the time if all three person work together
#formula used as per the question
combined = (x * y * z)/(x*y + y*z + x*z)
#rounding the answer to 2 decimal places for easy readability
days = round(combined,2)
#printing the total time taken by all three persons
print('Total time taken to complete work if A, B and C work together: ', days)
