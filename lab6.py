#Name: Jack Bui

#Lab 6 – Task 1
class   question():
    def __init__(self, dict, correct_answer):
        self.dict = dict
        self.correct_answer = correct_answer
    
    def print_question(self): #Interate through the dictionary and print the values 
        for key in self.dict.values():
            print(key) 
        return self.check_answer() #check if input by student object is correct

    def check_answer(self):
        user_input = input()
        if user_input.lower() == self.correct_answer:
            return True
        else:
            return False

class test():
    def __init__(self, list):
        self.list = list

    def take_test(self, student):
        print("\nWelcome to the test", student.name) #welcome message 
        for dictionary in self.list: #Loop through the list of dictionary questions to print the question and check answer
            if dictionary.print_question() == True:
                student.correct() #add 1 to the score of the student if their answer is correct 


class   student():
    def __init__(self, name, age, id, test_score = 0):
        self.name = name
        self.age = age
        self.id = id
        self.test_score = test_score

    def print_values(self): #print values of the student object 
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.id)
        print("Test Score:", self.test_score)
    
    def correct(self):  #Add one to the student object 
        self.test_score += 1
    
    def reset(self): #reset student object total score 
        self.test_score = 0 



def main():
    q1 = question({"question" : "Where is Cal Poly Pomona located?", "a" : "A. Texas" , "b" : "B. California",
         "c" : "C. Nevada", "d" : "D. Washington"}, "b")

    q2 = question({"question" : "On your student records system, what does CSU stand for?", "a" : "A. California State Universities" ,
    "b" : "B. Colorada State University", "c" : "C. Color Sparkling Unicorn", "d" : "D. Canadian Swan Upping"}, "a")

    q3 = question({"question" : "What is 5 + 5?", "a" : "A. 23" , "b" : "B. 15", "c" : "C. -23", "d" : "D. 10"}, "d")

    q4 = question({"question" : "How many moons does Earth have?", "a" : "A. 32" , "b" : "B. 3", "c" : "C. 1", "d" : "D. 0"}, "c")

    q5 = question({"question": "What lab is this?", "a" : "A. 3" , "b" : "B. 1", "c" : "C. 4", "d" : "D. 6"}, "d")

    
    test1 = test([q1,q2,q3,q4,q5]) #test object with selected question objects
    
    p1 = student("jack", 13, 1234) 
    p2 = student("james", 17, 4321) #Three student objects 
    p3 = student("jacob", 15, 2341)

    test1.take_test(p1) #student 1 take test 
    p1.print_values() #return student score after test
    test1.take_test(p2)# student 2 take test 
    p2.print_values() #return student score after test
    test1.take_test(p3)# student 3 take test 
    p3.print_values() #return student score after test

if __name__ == "__main__": #call main 
    main()


#output
"""
Welcome to the test jack
Where is Cal Poly Pomona located?
A. Texas
B. California
C. Nevada
D. Washington
b
On your student records system, what does CSU stand for?
A. California State Universities
B. Colorada State University
C. Color Sparkling Unicorn
D. Canadian Swan Upping
a
What is 5 + 5?
A. 23
B. 15
C. -23
D. 10
d
How many moons does Earth have?
A. 32
B. 3
C. 1
D. 0
c
What lab is this?
A. 3
B. 1
C. 4
D. 6
d
Name: jack
Age: 13
ID: 1234
Test Score: 5

Welcome to the test james
Where is Cal Poly Pomona located?
A. Texas
B. California
C. Nevada
D. Washington
a
On your student records system, what does CSU stand for?
A. California State Universities
B. Colorada State University
C. Color Sparkling Unicorn
D. Canadian Swan Upping
b
What is 5 + 5?
A. 23
B. 15
C. -23
D. 10
d
How many moons does Earth have?
A. 32
B. 3
C. 1
D. 0
c
What lab is this?
A. 3
B. 1
C. 4
D. 6
a
Name: james
Age: 17
ID: 4321
Test Score: 2

Welcome to the test jacob
Where is Cal Poly Pomona located?
A. Texas
B. California
C. Nevada
D. Washington
c
On your student records system, what does CSU stand for?
A. California State Universities
B. Colorada State University
C. Color Sparkling Unicorn
D. Canadian Swan Upping
c
What is 5 + 5?
A. 23
B. 15
C. -23
D. 10
c
How many moons does Earth have?
A. 32
B. 3
C. 1
D. 0
c
What lab is this?
A. 3
B. 1
C. 4
D. 6
c
Name: jacob
Age: 15
ID: 2341
Test Score: 1
"""