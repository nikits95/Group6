#
#Questionnaire part 1
#Honey and Mumford questionnaire module
#
from tkinter import *
import tkinter.messagebox
from CalResults import *

class Questionnaire(Frame):

	#list holding the answers
	answerList = []

	#def __init__(self,master):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.grid()
		self.createQuestions()
		self.createButton()
		self.createQuit()

	def createQuestions(self):
		#creating question1
		self.varQ1 = IntVar
		Q1 = Label(self,text="When Learning What an Object is in object orientated programming do you prefer :",font=("BOLD",13))
		Q1.grid(row=1, column=1, columnspan=4,sticky=W,padx=50,pady=10)

		#creating question1 answers
		self.varQ1 = IntVar()
		R1Q1 = Radiobutton(self, text="To role-play a scenario", variable=self.varQ1, value=4)#(Activist)
		R1Q1.grid(row=2, column= 2, sticky=W, padx=100)
		R2Q1 = Radiobutton(self,text="Read a book about the subject", variable= self.varQ1, value=3) #(Theorist)
		R2Q1.grid(row=3, column= 2, sticky=W, padx=100)
		R3Q1 = Radiobutton(self, text="Be given a relevant case study that applies in a working environment", variable= self.varQ1, value=2) #(Pragmatist)
		R3Q1.grid(row=4, column= 2, sticky=W, padx=100)
		R4Q1 = Radiobutton(self, text="Discuss in a group", variable= self.varQ1, value=1) #(Reflector)
		R4Q1.grid(row=5, column= 2, sticky=W, padx=100)

		#creating question2
		Q2 = Label(self,text="When given a task to develop a piece of software for an item of coursework, do you find it best to:",font=("BOLD",13))
		Q2.grid(row=10, column=1, columnspan=4,sticky=W,padx=50,pady=10)

		#creating question1 answers
		self.varQ2 = IntVar()
		R1Q2 = Radiobutton(self, text="Go straight into the problem with confidence of solving it", variable=self.varQ2, value=4)#(Activist)
		R1Q2.grid(row=11, column= 2, sticky=W, padx=100)
		R2Q2 = Radiobutton(self,text="Seek out some pre-existing software that is similar and use that as an example", variable= self.varQ2, value=1)#(Reflector)
		R2Q2.grid(row=12, column= 2, sticky=W, padx=100)
		R3Q2 = Radiobutton(self, text="Get into a team / group and collectively solve the problem together", variable= self.varQ2, value=3)#(Theorist)
		R3Q2.grid(row=13, column= 2, sticky=W, padx=100)
		R4Q2 = Radiobutton(self, text="Solving the problem over a period of time in small sections", variable= self.varQ2, value=2)#(Pragmatist)
		R4Q2.grid(row=14, column= 2, sticky=W, padx=100)

	def collectAnswers(self):
		radioAnswer1 = self.varQ1.get()
		radioAnswer2 = self.varQ2.get()
		Questionnaire.answerList.append(radioAnswer1)
		Questionnaire.answerList.append(radioAnswer2)
		#print([radioAnswer1, radioAnswer2])
		#print(Questionnaire.answerList)
		#stops the button from being accessed by the user
		self.btn.configure(state=DISABLED, text="Finished")
		print(Questionnaire.answerList)
		CalResults(Questionnaire.answerList,"H&M")
		#root.destroy()
		
	def getAnswers(self):
		return Questionnaire.answerList

	def quitQues(self):
		tkinter.messagebox.showinfo("Warning", "You are going to quit the questionnaire")
		quit()
	
	def createButton(self):
		self.btn = Button(self, text="Submit",command=self.collectAnswers)
		self.btn.grid(row=15, column=2)

	def createQuit(self):
		self.quitBtn = Button(self, text="Quit", command=self.quitQues)
		self.quitBtn.grid(row=16, column=3)

def main():
	window = Tk()
	window.title('Questionnaire')
	window.resizable(0,0)
	application = Questionnaire(window,"")
	window.mainloop()

if __name__ == "__main__":
	main()
