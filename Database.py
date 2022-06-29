import PySimpleGUI as sg


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
    database = {"jack": "password"}
    while True:             # Event Loop
        event, value = window.read()
        #print( event, value)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Enter':
            if value[0] not in database.keys() or value[1] != database[value[0]]:
                return_statement.update(value="The Username or password you entered does not exist or is incorrect")
        
    window.close()
    print(database)
if __name__ == '__main__':
    main()



