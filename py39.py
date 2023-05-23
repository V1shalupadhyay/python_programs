tup= ()

while True :
      num = int(input("Enter a number :- "))
      tup += (num,)
      user = input("Do you want to quit enter yes =")
      if user == "yes":
            print(tup)
            print("Max :-",max( tup ))
            print("Min :-",min( tup ))
            break
