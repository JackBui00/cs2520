#Name: Jack Bui 

#Lab 6 – Task 1
class   question():
    def __init__(self, dict, correct_answer):
        self.dict = dict
        self.correct_answer = correct_answer

    def print_question(self):
        for key in self.dict.values():
            print(key)  

    def check_answer(self, input):
        if input.lower() == self.correct_answer:
            return True
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

class   question4():
    question_dict = {"question" : "How many moons does Earth have?", "a" : "A. 32" , "b" : "B. 3", "c" : "C. 1", "d" : "D. 0"}
    answer = "c"

q1 = question({"question" : "Where is Cal Poly Pomona located?", "a" : "A. Texas" , "b" : "B. California",
         "c" : "C. Nevada", "d" : "D. Washington"}, "b")

q1.print_question()

print(q1.check_answer("c"))


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

input = "c"
q1 = question1()

p1 = student("jack", 13, 1234)

