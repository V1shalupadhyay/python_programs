def myMean(myList): #function to compute means of values in list
 total = 0
 count = 0
 for i in myList:
     total = total + i #Adds each element i to total
     count = count + 1 #Counts the number of elements
 mean = total/count #mean is calculated
 print("The calculated mean is:",mean)
myList = [1.3,2.4,3.5,6.9]
#Function call with list "myList" as an argument
myMean(myList)
