#Name: Jack Bui 

#Lab 4 – Task 1


#part A 

#Create list, user input 
def user_list():
    L1 = []

    i = 1
    while i < 5:
        user_input = float(input("Enter float value "+ str(i) + ": "))
        i += 1
        L1.append(user_input)
    #print(L1)
    return(L1)

#part B

#random list generate with random amount with random float values 
import random 
from sympy import *
def random_list():
    L2 = []
    size = random.randint(0,10)
    i = 1
    while i < size:
        L2.append(random.uniform(0,10))
    return L2

#part C 
def prime_value_list(size):
    L3 = []
    i = 1
    while i < size:
        if isprime(i):
            L3.append(i)
            print(i)
    i =+ 1
    return L3

print(prime_value_list(25))
