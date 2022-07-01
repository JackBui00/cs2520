import PySimpleGUI as sg
from cryptography.fernet import Fernet
from sympy import *
import csv  #maybe csv file


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

def make_new_user(database):
    return_statement = sg.Text()
    layout = [
        [sg.Text("Make New User")],
        [sg.Text("Username",size = (10,1)), sg.InputText()],
        [sg.Text("Password",size = (10,1)), sg.InputText()],
        [return_statement],
        [sg.Button("Enter"), sg.Button("Exit")]
    ]
    window = sg.Window("Create A New User", layout)
    while True:             # Event Loop
        
        event, value = window.read()
        #print( event, value)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Enter":
            if value[0] in database.keys():
                return_statement.update(value = "Username already exist")
                continue
            database[value[0]] = fernet.encrypt(value[1].encode())
            return_statement.update(value = "New User has been made")
    
    window.close()




def main():
    return_statement = sg.Text()
    layout = [
        [sg.Text("Login Screen")],
        [sg.Text("Username",size = (15,1)), sg.InputText()],
        [sg.Text("Password",size = (15,1)), sg.InputText()],
        [return_statement],
        [sg.Button("Enter"), sg.Button("Exit"),sg.Button("Make New User"),sg.Button("Forgot Password")]
    ]
    window = sg.Window("Login Portal", layout)

    database = {"jack": "wordpass","james": "password123", "german": "potato"}

    database = encrypt(database)

    while True:             # Event Loop
        
        event, value = window.read()
        #print( event, value)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Enter":
            if value[0] in database.keys():
                if fernet.decrypt(database[value[0]]).decode() == value[1]:
                    return_statement.update(value = "The password was correct")
            elif value[0].lower() not in database.keys() or value[1] != fernet.decrypt(database[value[0]]).decode():
                return_statement.update(value="The Username or password you entered does not exist or is incorrect")
        if event == "Make New User":
            make_new_user(database)
            
        if event == "Forgot Password":
            return_statement.update(value = fernet.decrypt(database[value[0]]).decode())

        
    window.close()
    print(database)
if __name__ == "__main__":
    main()



