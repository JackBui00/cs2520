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

#return list with prime values within the set parameter 
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
#find vowels of the string
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
#print(find_vowels())
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


#Lab 4 – Task 2

#part A 

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2, 1: 'wow', 20 : [3, 4, 5], (1, 2) : ['hi', 'bye']}
stuff[2520] = 'cpp'
print(stuff)
#output
'''
{'name': 'Zed', 'age': 39, 'height': 74, 1: 'wow', 20: [3, 4, 5], (1, 2): ['hi', 'bye'], 2520: 'cpp'}
'''

#part B 
favoriteFoods = {"Peg": "burgers", "Cy": "hotdogs", "Bob": "apple pie","Kim": "oranges","Arthur": "sandwich"}

for names in favoriteFoods:
    print(names + " Chooses " + favoriteFoods[names])
#output
'''
Peg Chooses burgers
Cy Chooses hotdogs
Bob Chooses apple pie
Kim Chooses oranges
Arthur Chooses sandwich
'''

#part C

def update(db, key, new_value):
    if key in db.keys():
        db[key] = new_value
    else:
        print("Thrown Error, key does not exist")
    return
     

def main():
    pwdDB = {'ted' : 'xxx', 'jan' : 123, 'kay' : '13yy'}
    print(pwdDB)
    update(pwdDB, 'ted', 'new value')
    update(pwdDB, 'wade', 'new value 2')
	#now, call update() function to update the pwdDB 
	#print(db)	#any change made to db? 
    print(pwdDB)
#main()
#output
'''
#output 1
{'ted': 'xxx', 'jan': 123, 'kay': '13yy'}
{'ted': 'new value', 'jan': 123, 'kay': '13yy'}

#output 2
{'ted': 'xxx', 'jan': 123, 'kay': '13yy'}
Thrown Error, key does not exist
{'ted': 'xxx', 'jan': 123, 'kay': '13yy'}
'''

#Lab 4 – Task 3

#part A 

#Create a set from a list
L = [1, 4, 9, 4, 7, 2, 2, 9]
S = set(L)
print(S)
print("The size is " + str(len(S)))
#output
'''
{1, 2, 4, 7, 9}
The size is 5
'''

#part B

S1 = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34}
S2 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
print(S1.union(S2))
print(S1.intersection(S2))
print(S1.symmetric_difference(S2))
#output
'''
{0, 1, 2, 3, 5, 7, 8, 11, 13, 17, 19, 21, 23, 29, 34} #Union 
{13, 2, 3, 5} #Intersection 
{0, 1, 34, 7, 8, 11, 17, 19, 21, 23, 29} # Symmetric Difference 
'''


#Lab 4 – Task 4

#part A 

#Create two list of Username + Password
from cryptography.fernet import Fernet

#names = [] #uncomment to enter each name and password individually 
#password = [] #uncomment {“Jesse” : “x11yz”, “Alex” : “hizzpp”
names = ["Jesse","Alex", "Betty", "Kim", "Jose", "Jones", "Jasmine"]   #Test names #comment out if using manual input 
password = ["x11yz","hizzpp", "1234","Kim", "password123", "burgendy", "rice"]  #Test names  #comment out if using manual input 

encryption_key = Fernet.generate_key()

fernet = Fernet(encryption_key)

#Ecrypt the password of dictionary 
def encrypt(target):
    for v in target.keys():
        target[v] = fernet.encrypt(target[v].encode())
    return target

#decrypt the password of dictionary 
def decrypt(target):
    for v in target.keys():
        target[v] = fernet.decrypt(target[v]).decode()
    return target
#print(encrypt(password))

#Take in user name and password individually 
def new_user():
    names.append(input("Enter your name: "))
    password.append(input("Input your password: "))
i = 0

#Enter each username by hand if wanted
#while i < 5: 
    #new_user()
    #i += 1

#zip password and username list into dictionary 
user_name_dict = dict(zip(names,password))
print(user_name_dict) #print decrypted 
user_name_dict = encrypt(user_name_dict)
print(user_name_dict) #Print ecrypted 
#output 
'''
{'Betty': '1234', 'Kim': 'Kim', 'Jose': 'password123', 'Jones': 'burgendy', 'Jasmine': 'rice'}
'''

def login():
    i = 0
    user_name_input = input("Enter your username: ")
    if user_name_input in user_name_dict.keys():
        while i < 3:
            password_input = input("Enter your password: ")
            if password_input == fernet.decrypt(user_name_dict[user_name_input]).decode():
                print("You have logged in!")
                request_change_pass = input("Do you want to change password? (Yes or No): ").lower()
                if request_change_pass == "yes":
                    change_password(user_name_input)
                    break
                else:
                    break
            elif password_input == "0":
                break
            else: 
                print("Wrong password, try again")
                i += 1
                print( str(i) + " Wrong try")     
        print("You failed all 3 times!")  
        login()
    elif user_name_input == "0":
        return
    else:  
        login()

def change_password(user_name):
    unenrypted_password = str(input("Enter a new password: "))
    encrypted_password = fernet.encrypt(unenrypted_password.encode())
    user_name_dict[user_name] = encrypted_password

login()
login()
#print(decrypt(user_name_dict)) #print decrypted with new password change 
user_name_dict = decrypt(user_name_dict)
print(user_name_dict)
user_name_dict = encrypt(user_name_dict)
print(user_name_dict)
#print(user_name_dict)
#print(encrypt(user_name_dict)) #print encrypted username and password dictionary 
#output
'''
#Dictionary unecrypted, Unchanged without password edit by user 
{'Jesse': 'x11yz', 'Alex': 'hizzpp', 'Betty': '1234', 'Kim': 'Kim',
 'Jose': 'password123', 'Jones': 'burgendy', 'Jasmine': 'rice'}

#Dictionary password Encrypted
{'Jesse': b'gAAAAABirmeyUucmCG6gs0UCC7WFZhNOi3wUZWdFuGOSEwMojF43SHmfLxMUW1qeITk8VmQGaqedbGnlEysQvKSMPhA0S59jig==',
'Alex': b'gAAAAABirmeyclhhZYdFCM9YMHQRgX1nwe-UJqOLlt1TfhCSvlp1FC6Xf36C3s-C7Y4JieOBQ6P-lbKj7nKuDfzYewUhZF0c6A==',
'Betty': b'gAAAAABirmeyB28HwY1UZyLE3AwmH2kPEEhXMH9IrU7BAzyfSo2ZKkrbAPuGhaoY3PWj_Vegw4fQoKgGMpluqzUijyjFcaavHg==',
'Kim': b'gAAAAABirmeyVElEkTfym4GW7obxSeZllV4-e-iDbfl4wLr53yEeWMP32Fjslc2J1rl-9-WtI1Xe3kudy0E7GcYsRl_IR3e4lg==',
'Jose': b'gAAAAABirmeyznZufEYiD35qCnB941EqguOgDkQ3kxiK8-D2CAIoz96_Fo3rnQiOZAlej0VGRbWubNbqaVDle-f8sQMZRpk7tw==',
'Jones': b'gAAAAABirmey_G3xa_r1fHgapIHSKoLpjg_RwXoyaUy0UHWiPOOh_W7bcSHi3IU6_brpnVdLajm6uCOS_GZVV3__19BKN4ICmQ==',
'Jasmine': b'gAAAAABirmeyJQVvJtaOoNHIX82b-RoDUQSoPDWeEIxAYfQrXWcx5eCZ-AFoRWdSR5OR-AII4CzOGK0iWGsVk6LwTbORISBcZg=='}

#Login First try 
Enter your username: Jesse
Enter your password: x11yz
You have logged in!

#Login 3rd try 
Enter your username: Jesse
Enter your password: 1234
Wrong password, try again
1 Wrong try
Enter your password: 1234
Wrong password, try again
2 Wrong try
Enter your password: x11yz
You have logged in!

#Failed Login 3 times 
Enter your username: Jesse
Enter your password: 1234
Wrong password, try again
1 Wrong try
Enter your password: hello
Wrong password, try again
2 Wrong try
Enter your password: potato
Wrong password, try again
3 Wrong try
You failed all 3 times!
Enter your username:

#Login user, change password
Enter your username: Jesse
Enter your password: x11yz
You have logged in!
Do you want to change password? (Yes or No): yes
Enter a new password: corn


#Input to change password 
Enter your username: Jesse
Enter your password: x11yz
You have logged in!
Do you want to change password? (Yes or No): yes
Enter a new password: corn
Enter your username: Alex
Enter your password: hizzpp
You have logged in!
Do you want to change password? (Yes or No): yes
Enter a new password: purpleflower
Enter your username: 0
Enter your username: 0

#Dictionary with new passwords unecrypted 
{'Jesse': 'corn', 'Alex': 'purpleflower', 'Betty': '1234', 'Kim': 'Kim',
'Jose': 'password123', 'Jones': 'burgendy', 'Jasmine': 'rice'

#Dictionary with new password encrypted
{'Jesse': b'gAAAAABirm_C_T-Y54pTy-cV_wClW-v0VgisvfNLr3xyAC0ueNVo0L5GnLVSzsqftacSptQyltzVcEDgmftKFbTtJfSny_iG4w==', 
'Alex': b'gAAAAABirm_CSFlQ4heoKmbRHOSn6C7KaI0lCUDGmCeI-uevcS5RUAgq-BYAdp1VxJlThz-_jIy6dcNo9NraQy3KR3JXLsxO9A==', 
'Betty': b'gAAAAABirm_CozCGYNqHIeir-8TrFQ7kmQdmMBZh4x_jZcZ5AaNaLP3L-Eppbx5NG7n8kaxXr2qnJLq0thtLqg10d475I_RuQg==', 
'Kim': b'gAAAAABirm_CeguV25WSVpCuZvX35_9MCRw2Nq6w34XtYuxoy1xods1EeWrcNycAFCveQ5vRGZ1w3LLxOhIxpHdchv09-6lAyQ==', 
'Jose': b'gAAAAABirm_CNnczLkNb06KKWpjJ8Alid9Dj_734_34DUglKQWotN1u8nfTFPmbau5EIE457_4JNbiNUPjnJLITuigDutVu1Zw==', 
'Jones': b'gAAAAABirm_C-CUogl9QoPFaV2jhidNz_kwbg4jV5cEWHCya7GOAsO49N7gDvzZzURJO-sdTC7IROlGMsJMGnv4jWELmFC7osg==', 
'Jasmine': b'gAAAAABirm_CMPWOnJuurMlo6lh5WN4Bxg89Rp-4_Y9AOzQv03YU9xb0oWMGUz773JvhR75lw6uh5F_Wuuwi1r6IbYBYCrqDUg=='}



'''