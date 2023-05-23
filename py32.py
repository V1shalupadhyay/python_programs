# Python3 program to print reverse 
# of words in a string. 

def wordReverse(str): 
	i = len(str)-1
	start = end = i+1
	result = '' 

	while i>=0: 
		if str[i] == ' ': 
			start = i+1
			while start!= end: 
				result += str[start] 
				start+=1
			result+=' '
			end = i 
		i-=1
	start = 0
	while start!=end: 
		result+=str[start] 
		start+=1
	return result 

# Driver Code 
str = input("Enter string: " )
print(wordReverse(str)) 

# This code is contributed 
# by SamyuktaSHegde 
