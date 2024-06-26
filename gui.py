import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter To-Do")
text_box = sg.InputText(tooltip="To-Dos")
add_button = sg.Button("Add")

window = sg.Window("My To-Dos App", layout=[[label],[text_box,add_button]])
window.read()
window.close()