import FreeSimpleGUI as sg #sg is short form , pip is python ka package manager
from functions import read_todo,write_todo
import time
import os
if not os.path.exists("todo.txt"):
    with open ("todo.txt","w") as file:
        pass #interpretator ko next line mein bhej dega cox with ke baad code likhna hota hai but we had nothing
# sg.theme("DarkBlue12")
# pip is installing , import se use kar rahe hai after installation
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo" , key="todo") # curser leyaoge toh chota sa impromt aageya "enter a todo"
list_box = sg.Listbox(values=read_todo(), size=(45,10) ,
                    key="todos",enable_events=True)
clock=sg.Text("",key="clock")
add_button= sg.Button("Add")
edit_button = sg.Button("Edit")
delete_button=sg.Button("Delete")
exit_button = sg.Button("Exit")
window= sg.Window("My To-Do App",
                  layout=[[clock],[label,input_box,add_button],[list_box,edit_button,delete_button,exit_button]],
                  font=("Arial",14)) # Window is a class jiska humesha ek object hoga
#list of list coz visual hierarchy ...ek ke neeche ek
while True:
    event,value = window.read(timeout=200) #event is a variable which is going to store the output of read method ----tuple
# read is a method of "Window" class , uss Window mein jo commands hai woh read acccess karega
    window["clock"].update(value=time.strftime("%b %d , %Y , %H:%M:%S"))
     #value is dictionary part . pass the kwy to access that particular value []
    match event:
        case "Add":
            todos = read_todo()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='') #value ek hi hai
        case "Edit":
            try:
                todos=read_todo()
                todo_to_edit= value['todos'][0]
                index = todos.index(todo_to_edit)
                new_todo = value['todo']
                todos[index] = new_todo
                write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a todo to edit",font=("Arial",14)) #popup se input box pe show karega
        case "Delete":
            try:
                todos=read_todo()
                todo_to_delete=value['todos'][0]
                todos.remove(todo_to_delete)
                write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='') #yaha pe null kardo , input box mein
            except IndexError:
                sg.popup("Please select a todo to delete",font=("Arial",14))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WINDOW_CLOSED:
            break
# exit() pure code ko exit karega whereas break stop karega . exit ke baad neeche wali lines run nahin hogi

window.close()
# DE-COUPLING=ek value ko alag alag variable mein dena