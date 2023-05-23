# n = 3 Number of lines from top to middle of diamond shape
n =6
for i in range (1, n + 1):
          # This will print the space  
    space = (n - i)*" "
          # It will print the star
    star =  ( 1* i - 1)*"*"
    print(star,space)
