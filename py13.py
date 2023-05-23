#Program to print the table of a number
num = int(input("Enter the number to display its table: "))
print("Table: ");
for a in range(1,11):
    print(num," × ",a," = ",(num*a))
