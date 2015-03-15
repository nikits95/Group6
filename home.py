from tkinter import *
class home(Frame):
	def _init__(self,master):
		Frame.__init_(self,master)
		#call the methods for creating the Labels, buttons, etc here
		#e.g. self.createHomeButtons()

	def createHomeButtons(self):
		#Creates Tk buttons
		#One that leads to the first questionnaire
		#The other that will move to the COMSC part

	def createHomeLabels(self):
		#creates the 3 main labels for the Frame
		#One for instructions
		#Another to instruct COMSC to click Admin buttom

	def moduleProgram(self):
		#produces a list of all the modules in COMSC
		#Similar to the one on the sheet
		#When clicked along with the start questionnaire button, it should save the degree program. 
		lblProg = Label(self, text='Degree Programme:', font=('MS', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=2, sticky=N)

		self.listProg = Listbox(self,height= 3)
		scroll = Scrollbar(self, command= self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)

		self.listProg.grid(row=0, column=2,columnspan=2,sticky=N)
		scroll.grid(row=0, column=4, sticky=W)

		for item in ["Computer Science", "Software Engineering","BIS",""]:
			self.listProg.insert(END, item)
		
		self.listProg.selection_set(END)

	#add any more methods if needed
