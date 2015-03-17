from tkinter import *
from Home import *

class Controller(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master

		self.cont_frame = Frame(self.root)
		self.cont_frame.pack(side=LEFT, padx=5, pady=5)

		homepage = Home(self.cont_frame)
		homepage.pack(side=LEFT, padx=20, pady=20)

		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(homepage))
		self.btnHome.pack(side=LEFT)

	def gettingHomeData(self, currentframe):
		(yearOfStudy,degreeProgram) = currentframe.get_information()
		print(yearOfStudy,degreeProgram)
		currentframe.destroy()
		self.btnHome.destroy()

		#honey = Questionnaire(self.cont_frame) #the first questionnaire needs 
		#honey.pack()							#to go here



root = Tk()
app = Controller(root)
root.mainloop()