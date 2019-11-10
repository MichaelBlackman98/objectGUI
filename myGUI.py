import PySimpleGUI as sg
import objectmaker 

#each bracket represents a row on the window
layout =    [ 
              [sg.Text('click a button below to print an object to the terminal!!!')],
              [humanbutton = sg.Button('human button')],
              [catbutton = sg.button('cat button')]

            ]

window = sg.Window('Window Title', layout)



while True:
    event, values = window.read()
    
    
   
        







#################################################################

#I want this gui to generate some objects from seperate files.

#################################################################