from Choice import *
from Question import *
from Application import * 
from Questionnaire import * 
from tkinter import *

# Starting the app ********************************************

root = Tk()
root.geometry("1000x300")
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
app = Application(master=root, VQuest=Questionnaire1, HMQuest=Questionnaire2)
root.mainloop()
root.destroy()
