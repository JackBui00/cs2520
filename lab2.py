#Name: Jack Bui 

#Lab 2 – Task 1
#This program will calculate the average cost per item purchased

count = int(input("Enter how many items you purchased: "))
total = int(input("Enter the total cost: "))
print("Average =", total/count if count != 0 or total != 0 else "NA")
#output
'''
#output 1 
Enter how many items you purchased: 0
Enter the total cost: 0
Average = NA

#output 2
Enter how many items you purchased: 25
Enter the total cost: 50
Average = 2.0
'''

#Lab 2 - Task 2 

#This program will compute and display the sum of values 
#Part A 

sum = 0 
for x in range(20):
    sum = sum + x 
print(sum)
#output
'''
190
'''

#Part B 
#while(True):
   # print("Infinite While Loop")
#output
'''
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
Infinite While Loop
'''

#Part C 
value = 0
prime_input = int(input("Enter a number to check if it is prime or not: "))
i = 2
while(i < prime_input/2):
    if(prime_input % i == 0):
        value += 1
        break
    i += 1 
print("The value",prime_input, "is a prime number" if value == 0 else "is not a prime number")
#output
'''
output 1
Enter a number to check if it is prime or not: 37
The value 37 is a prime number

output 2 
Enter a number to check if it is prime or not: 35
The value 35 is not a prime number
'''

#Lab 2 - Task 3
#This Program will calculate the BMI of the user and return if their BMI is below, inside, or above the normal BMI range 
import re

user_system_choice = input("Would you like use metric(1) or imperial(2): ")
user_weight = input("Input the weight: ")
user_weight = float(re.search(r'\d+', user_weight).group())
user_height = input("Input Height: ")
user_height= float(re.search(r'\d+', user_height).group())
match user_system_choice:

    case "1":
        bmi = user_weight/(user_height**2)

    case "2":
        bmi = 703 * user_weight/(user_height**2)

if bmi < 18.5:
    print("The BMI of " + str(round(bmi,2)) + " is considered underweight.")
elif bmi > 25.9:
    print("The BMI of " + str(round(bmi,2)) + " is considered overweight.")
else: 
    print("The BMI of " + str(round(bmi,2)) + " is considered normal.")

#output
'''
#output 1
Would you like use metric(1) or imperial(2): 1
Input the weight: 75kg
Input Height: 1.65m
The BMI of 75.0 is considered overweight.

#output 2
Would you like use metric(1) or imperial(2): 1
Input the weight: 120kg
Input Height: 1.82m
The BMI of 120.0 is considered overweight.

#output 3
Would you like use metric(1) or imperial(2): 2
Input the weight: 105
Input Height: 75
The BMI of 13.12 is considered underweight.

#output 4
Would you like use metric(1) or imperial(2): 2
Input the weight: 200lbs
Input Height: 75.5
The BMI of 25.0 is considered normal.

#output 5
Would you like use metric(1) or imperial(2): 2
Input the weight: 130lbs
Input Height: 71inches
The BMI of 18.13 is considered underweight.
'''

#Lab 2 - Task 3
#This program is an algorithm that interates to calculate the squareroot
import math 

def find_square_root(guess,counter):
    new_check = ((guess + s_value / guess) / 2)
    while round(new_check,3) != round(true_value,3):
        counter += 1
        find_square_root(new_check, counter)

    
    print("answer found after " + str(counter) + " interations!")
    print(round(new_check,3))
    exit()

s_value = float(input("Input a value to find the square root: "))
initial_guess = float(input("Make a guess of any positive value: "))
true_value = math.sqrt(s_value)
find_square_root(initial_guess, 0)
#output
'''
#output 1
#Input a value to find the square root: 9.0
Make a guess of any positive value: 2
answer found after 2 interations!
3.0

#output 2
Input a value to find the square root: 21.5
Make a guess of any positive value: 4
answer found after 1 interations!
4.637

#output 3
Input a value to find the square root: 47.0
Make a guess of any positive value: 2
answer found after 4 interations!
6.856

#output 4
Input a value to find the square root: 249.23
Make a guess of any positive value: 3
answer found after 4 interations!
15.787

'''

