import PySimpleGUI as sg
from cryptography.fernet import Fernet

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

def main():
    return_statement = sg.Text()
    layout = [
        [sg.Text("Login Screen")],
        [sg.Text("Username",size = (15,1)), sg.InputText()],
        [sg.Text("Password",size = (15,1)), sg.InputText()],
        [return_statement],
        [sg.Button("Enter"), sg.Button("Exit")]
    ]
    window = sg.Window('Login Portal', layout)

    database = {"jack": "password","james": "password123", "german": "potato"}

    database = encrypt(database)

    while True:             # Event Loop
        event, value = window.read()
        #print( event, value)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Enter':
            if value[0].lower() not in database.keys() or value[1] != fernet.decrypt(database[value[0]]).decode():
                return_statement.update(value="The Username or password you entered does not exist or is incorrect")
            elif fernet.decrypt(database[value[0]]).decode() == value[1]:
                return_statement.update(value = "The password was correct")
        
    window.close()
    print(database)
if __name__ == '__main__':
    main()



