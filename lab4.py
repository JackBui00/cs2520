#Name: Jack Bui 

#Lab 4 – Task 1


#part A 

#Create list, user input 
def user_list():
    L1 = []
    i = 1
    while i < 50:
        user_input = float(input("Enter float value "+ str(i) + ": "))
        if user_input <= 0: #Break if userinput is 0 or below 
            break
        i += 1
        L1.append(user_input)
    #print(L1)
    return(L1)
#print(user_list())
#output
'''
#output 1
Enter float value 1: 10.2
Enter float value 2: 20.1
Enter float value 3: 15.2
Enter float value 4: 0
[10.2, 20.1, 15.2]

#output 2
Enter float value 1: 1.2
Enter float value 2: 2.3
Enter float value 3: 3.4
Enter float value 4: 4.5
Enter float value 5: 5.6
Enter float value 6: 0
[1.2, 2.3, 3.4, 4.5, 5.6]
'''



#part B

#random list generate with random amount with random float values 
import random 
from sympy import *
def random_list():
    L2 = []
    size = random.randint(0,10)
    i = 1
    while i < size:
        L2.append(round(random.uniform(0,10),2))
        i += 1
    return L2
#print(random_list())
#output
'''
#output 1
[2.87, 1.89, 4.41, 0.46, 8.26, 6.19, 7.58, 4.66, 9.8]

#output 2 
[9.53, 8.73, 6.29, 4.53, 2.66, 9.48, 0.87, 4.13]
'''

#part C 
def prime_value_list(start, end):
    L3 = []
    i = start
    while i < end:
        if isprime(i) == True:
            L3.append(i)
        i += 1
    return L3
#print(prime_value_list(50, 400))
#output
'''
#output 1 2-500
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 
149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

#output 2 50-400
[53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
'''

#part d 
import re 
def find_vowels():
    vowel = ["a","e","i","o",'u']
    user_input = input("Enter a string to check for vowels: ").replace(' ', '')
    L4 = []
    for char in user_input:
        L4.append(char.lower())
    L4 = tuple(L4)
    amount_of_vowel = 0
    for char in L4:
        if char in vowel:
            amount_of_vowel += 1
    print(L4)
    return amount_of_vowel
print(find_vowels())
#output
'''
#output 1
Enter a string to check for vowels: hello
('h', 'e', 'l', 'l', 'o')
2

#output 2
Enter a string to check for vowels: How many vowels are in this string
('h', 'o', 'w', 'm', 'a', 'n', 'y', 'v', 'o', 'w', 'e', 'l', 's', 'a', 'r', 'e', 'i', 'n', 't', 'h', 'i', 's', 's', 't', 'r', 'i', 'n', 'g')
9
'''


