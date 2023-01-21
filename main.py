from tkinter import *
from tkinter import messagebox
import tkinter as tk
# import os
import subprocess

def open_my_info():
    messagebox.showinfo("Team Details","Name : Anjaneya Mustoor\n Reg no: 21GANSD001\n""Name :  Gajendra M\n Reg no: 21GANSD002\n" )
    
def open_program():
    # os.system("qui.py")
    text = tk.Text(root)
    text.pack()
    with open("main.py", "r") as f:
        program_text = f.read()
        text.insert(tk.END, program_text)
    
def run_program():
    subprocess.run(["python","qui.py"])   

root=Tk()
root.title('Python-Assignment')
root.geometry("1000x1000+200+200")
Label(root,text="Quiz Application Using Python Tkinter",font=("Roboto",30)).pack()

Button(root,text="Student Details",height = "2", width = "30",font = ("Roboto",14),command=open_my_info).place(x=150,y=100)
Button(root,text="Open the Program",height = "2", width = "30",font = ("Roboto",14),command=open_program).place(x=150,y=200)
Button(root,text="Run the Program",height = "2", width = "30",font = ("Roboto",14),command=run_program).place(x=150,y=300)

root.focus_force()
root.mainloop()