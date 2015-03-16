from tkinter import *
class DisplayResults(Frame):
	def __init__(self,master, result):
		Frame.__init__(self,master)
		self.result = result
		self.showOnScreen(self.result)

	def showOnScreen(self, result):
		data = Label(text=result)
		data.pack()