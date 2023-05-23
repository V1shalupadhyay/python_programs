# Python3 Program to find sum of first n natural numbers 
# Return the sum of first n natural numbers 
def MY_SUM(n) : 
	sm = 0
	for i in range(1, n+1) : 
		sm = sm + (i) 
	
	return sm 
# Driven Program 
n = int(input("Enter Number"))
print(MY_SUM(n)) 
