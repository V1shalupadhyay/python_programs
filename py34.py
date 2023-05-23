#Function to increment the elements of the list passed as argument
def increment(list2):
    for i in range(0,len(list2)):
        list2[i] += 5
        print('Reference of list Inside Function',id(list2))
        #end of function
list1 = [5,15,25,35,45]
print("The list before the function call")
print(list1)
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)
