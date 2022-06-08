from cmath import e, pi
import math 
#Name: Jack Bui 

#Lab 1 – Task 1
#This program will display my dream job goal settings 
name = input("Please enter your name: ")
age = input("Please enter your age: ")
company = input("Enter the company you wish to work for: ")
salary = input("Enter monthly salary you wish to earn in dollars: ")
salary = int(salary) * 12
print("My name is " + str(name) + ",my age is",age) 
print("I wish to work for",company,"and earn $" + str(salary))

#output 
'''
#output 1
Please enter your name: Jack Bui 
Please enter your age: 20
Enter the company you wish to work for: Google
Enter monthly salary you wish to earn in dollars: 10500
My name is Jack Bui ,my age is 20
I wish to work for Google and earn $126000

#output 2 
Please enter your name: James Jockle 
Please enter your age: 2
Enter the company you wish to work for: Apple
Enter monthly salary you wish to earn in dollars: 8500
My name is James Jockle ,my age is 2
I wish to work for Apple and earn $102000
'''

#Lab 1 – Task 2
#This program will do calculations of values 

#1.	Find the average age of six people whose ages are 18, 19, 22, 23, 30, 17 respectively
age_of_people = [18,19,22,23,30,17]
average = sum(age_of_people)/len(age_of_people)
print ("average age =",average)
#output
'''
average age = 21.5
'''
#2.	Compute 2 to the 120th power. Note: do not use math module.
answer = pow(2,120)
print("2 to the power of 120 is",answer)
#output
'''
2 to the power of 120 is 1329227995784915872903807060280344576
'''
#3.	Calculate the square root of 31. Note: may import math 

answer2 = math.sqrt(31)
print("The squareroot of 31 is %.2f" %answer2)
#output
'''
The squareroot of 31 is 5.57
'''
#4.	Compute “hello_” * 3
answer3 = "hello_" * 3 
print(answer3)
#output
'''
hello_hello_hello_
'''
#5.	Enter a sentence, display how many characters 
# (including spaces and punctuations) 
# in this sentence, e.g. “how are you?” -> 12.  
sentences = ["how are you?","There are many birds in the sky!"]
for strings in sentences:
    print("The length of the string (" + strings + ") is",len(strings), "characters.")
#output
'''
The length of the string (how are you?) is 12 characters.
The length of the string (There are many birds in the sky!) is 32 characters.
'''

#Lab 1 – Task 3
#This program will do calculations of values and string concatenation

#1.	Input your first name (say, Jack) and your last name (say, Cray), 
# then create a string of your full name with a space separating 
# first and last name (i.e. Jack Cray), and output the full name. 

first = input("Enter your first name: ")
last = input("Input your last name: ")
print("Your full name is",first,last)
#output
'''
#output 1 
Enter your first name: Jack
Input your last name: Cray
Your full name is Jack Cray

#output 2
Enter your first name: Jack
Input your last name: Bui
Your full name is Jack Bui
'''

#2.	Assume you work in a kindergarten, input number of apples you 
# purchased as well as number of kids in a classroom. Output how 
# many apples (a whole number) each kid would get, and how apples 
# remaining (if not fully divisible among kids). E.g. 25 applies, 7 kids.

apples = input("Input number of apples purchased: ")
kids = input("Input number of students: ")
apples_per_kid = int(apples)//int(kids)
remaining_apples = int(apples) % int(kids)
print("Each kid would get", str(apples_per_kid), "with", str(remaining_apples),"remaining.")
#output
'''
#output 1 
Input number of apples purchased: 25
Input number of students: 5
Each kid would get 5 with 0 remaining.

#output 2 
Input number of apples purchased: 21
Input number of students: 4
Each kid would get 5 with 1 remaining.
'''
#3.	Enter x and y as two float numbers (e.g. x=3.5, y=4.2),
#  use one assignment statement to swap the values of these 
# two variables (i.e. now  x=4.2, y=3.5).  No additional variable 
# should be introduced. Note: Python has multiple/parallel assignment feature.

x = input("Input x: ")
y = input("Input y: ")
x, y = y, x 
print("x =", x,"and y =",y)
#output 
'''
#output 1
Input x: 1
Input y: 2
x = 2 and y = 1

#output 2
Input x: 25
Input y: 63
x = 63 and y = 25
'''

#4. Write code to calculate (a+b)/bc and display result. 
# Given test: the values of a, b, c are 2.5, 3.0, and 5.2 respectively.  
a = float(input("Input a: "))
b = float(input("input b: "))
c = float(input("Input c: "))
print("a+b/bc equals:", a+b/b*c)
#output
'''
#output 1
Input a: 2.5
input b: 3.0
Input c: 5.2
a+b/bc equals: 7.7

#output 2
Input a: 3.1
input b: 4.1
Input c: 1.4
a+b/bc equals: 4.5
'''

#5.	The Python math module has two constant values pi and e. Use Python output 
# format string to display these two values in the form of “pi = 3.14, e = 2.718”, 
# i.e. pi take two digits after decimal point while e takes 3 digits after decimal 
# point. Note: must use Python features such as format string, %, .2f  etc.

print("pi = {:.2f}" .format(math.pi))
print("e = {:.3f}" .format(math.e))
#output 
'''
pi = 3.14
e = 2.718
'''