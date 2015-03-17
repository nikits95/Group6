from tkinter import *
from Home import *
from Questionnaire import *

class Controller(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master

		cont_frame = Frame(self.root)
		cont_frame.pack(side=LEFT, padx=5, pady=5)

		homepage = Home(cont_frame)
		homepage.pack(side=TOP, padx=20, pady=20)
		
		btn = Button(cont_frame, text="Submit", command= lambda: self.homeData(homepage))
		btn.pack()

	def homeData(self, f):
		(a,b) = f.get_information()
		print(a,b)
		f.destroy()
		self.nextQues()



root = Tk()
app = Controller(root)
root.mainloop()