#import the math module, to use sin & radians function
import math
length = int(input("Enter the length of the ladder: "))
degrees = int(input("Enter the alignment degree: "))
#Converting degrees to radian
radian = math.radians(degrees)
#Computing sin value
sin = math.sin(radian)
# Calculating height and rounding it off to 2 decimal places
height = round(length * sin,2)
#displaying the output
print("The height reached by ladder with length",length,"feet and aligned at",degrees,"degrees is",height, "feet.")
