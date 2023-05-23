#Program to tell the user when they will turn 100 Years old
name = input("Enter your name: ")

# age converted to integer for further calculation
age = int(input("Enter your age: "))

#calculating the 100th year for the user considering 2020 as the current year
hundred = 2020 + (100 - age)

#printing the 100th year
print("Hi",name,"! You will turn 100 years old in the year",hundred)
