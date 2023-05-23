n = 5
for i in range (n,0,-1):
    #This will print the space before the number
    space = (n - i) * "  "
    print(end = " " ) 
    #This for loop will print the increasing numbers
    for j in range(1, i + 1):
        print(j, end = " ")
    #Print a new line after the space and numbers are printed
    print()
