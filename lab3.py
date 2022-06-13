#Name: Jack Bui 

#Lab 3 – Task 1

#This program will return if the integer is negative, positive or 0 
#part A 

import string
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
def output_without_whitespace(String = "This is a test case for the remove of the white spaces.\n"):
    String = re.split(' ', String)
    final_result_one = ''
    for x in String:
        final_result_one = final_result_one + str(x)
        #print(str(x), end= '')
    return final_result_one

#This function will create an acryonym of the phrase
def get_acronym(String2 = "This is another test of the things that can happen with it."):
    String2 = re.split(' ', String2)
    final_result_two = ''
    for y in String2:
        final_result_two = final_result_two + str(y[0])
        #print(str(y[0]), end='')
    return final_result_two.upper()

def main():
    user_input_one = str(input("\nEnter the first sentence to remove all the white space: "))
    print(output_without_whitespace(user_input_one))
    user_input_two = str(input("\nEnter the phrase that you want an acronym for: "))
    print(get_acronym(user_input_two))

main()
#output
'''
Enter the first sentence to remove all the white space: The only thing we have to fear is fear itself.
Theonlythingwehavetofearisfearitself.

Enter the phrase that you want an acronym for: random access memory
RAM
'''

#Lab 3 – Task 3

import lab3_DigitPrint as dp

#Take user input for the barcode
def take_barcode():
    barcode = input("Input a barcode: ")
    barcode = barcode.replace('-','')
    return barcode

#Splices and creates a list of the zipcode values, including the check_sum value to the end, returns list 
def check_sum(barcode):
    barcode_breakdown=[]
    for integer in barcode:
        barcode_breakdown.append(int(integer))
    barcode_breakdown.append(10 - sum(barcode_breakdown) % 10)
    return barcode_breakdown

#draws out the barcode that's to be created with the key 
def print_barcode_main(barcode_breakdown):
    key =[[1,1,0,0,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0],[0,1,0,0,1],[0,1,0,1,0],[0,1,1,0,0],[1,0,0,0,1],[1,0,0,1,0],[1,0,1,0,0]]
    dp.print_start()
    #loop though the zipcode + sum check 
    for value in barcode_breakdown:
        #loop through the list inside the key list to complete the correct code commands for the zip integer value 
        for value_two in key[value]:
            if value_two == 0:
                dp.print_zero()
            else:
                dp.print_one()
    dp.print_end()
    return None 

print_barcode_main(check_sum(take_barcode()))

#output
'''
output is in the pdf files named after the zip input
'''
        


