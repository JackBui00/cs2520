#Name: Jack Bui 

#Lab 3 – Task 1

#This program will return if the integer is negative, positive or 0 
#part A 

from turtle import pos


def posNegZero(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

#This program will compute the cube of the values 
#part B

def sqrCube(n = 5, m = 3):
    return(n**2, m**3)

#This program will call the functions sqrcube and posNegZero
#Part C 
print("posNegZeroCalls")
print(posNegZero(-5))
print(posNegZero(0))
print(posNegZero(6.5))

print("Square/Cube calls")
print(sqrCube())
print(sqrCube(4))
print(sqrCube(3,5))
print(sqrCube(n=4,m=2))
#print(sqrCube(n=4,2))
#output
'''
posNegZeroCalls
-1
0
1
Square/Cube calls
(25, 27)
(16, 27)
(9, 125)
(16, 8)

#Error message for last one
    print(sqrCube(n=4,2))
                       ^
SyntaxError: positional argument follows keyword argument
'''

#Lab 3 – Task 2

#This function is output_without_whitespace(), takes a string and prints without spaces(white space)
import re 
def output_without_whitespace(String):
    




        


