#Name: Jack Bui 

#Lab 6 – Task 1


class   question1():
    question_dict = {"question" : "Where is Cal Poly Pomona located?", "a" : "A. Texas" , "b" : "B. California",
         "c" : "C. Nevada", "d" : "D. Washington"}
    answer = "b"

class   question2():
    question_dict = {"question" : "On your student records system, what does CSU stand for?", "a" : "A. California State Universities" ,
    "b" : "B. Colorada State University", "c" : "C. Color Sparkling Unicorn", "d" : "D. Canadian Swan Upping"}
    answer = "a"

class   question3():
    question_dict = {"question" : "What is 5 + 5?", "a" : "A. 23" , "b" : "B. 15", "c" : "C. -23", "d" : "D. 10"}
    answer = "d"

def print_question(target):
        for key in target:
            print(key)  

def check_answer(input, answer):
    if input.lower() == answer:
        return True

class   student():
    def __init__(self, name, age, id, test_score = 0):
        self.name = name
        self.age = age
        self.id = id
        self.test_score = test_score

    def print_values(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.id)
        print("Test Score:", self.test_score)
    
    def correct(self):
        self.test_score += 1
    
    def reset(self):
        self.test_score = 0 


p1 = student("jack", 13, 1234)