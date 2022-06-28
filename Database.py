import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text("Login Screen")],
        [sg.Text("Username",size = (15,1)), sg.InputText()],
        [sg.Text("Password",size = (15,1)), sg.InputText()],
        [sg.Button("Enter"), sg.Button("Exit")]
    ]
    window = sg.Window('Login Portal', layout)
    database = {}
    while True:             # Event Loop
        event, value = window.read()
        #print( event, value)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Enter':
            if value[0] not in database.keys():
                print("Does not exist")
                database[value[0]] = value[1]
        
    window.close()
    print(database)
if __name__ == '__main__':
    main()



