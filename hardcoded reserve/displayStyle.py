from tkinter import *

class displayStyle(Frame):
	def __init__(self, master, learningType, QuestionnaireType):
		Frame.__init__(self, master)
		self.grid()
		l = Label(self,text="Your learning style for "+ QuestionnaireType + "\n is " + learningType, font=("Helvetica", 30, "bold italic"))
		l.pack()

##### test code ######

def main():
	root = Tk()
	app = displayStyle(root, "Visual", "VARK")
	root.mainloop()

if __name__ == "__main__":
	main()