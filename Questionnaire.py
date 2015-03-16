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
	def __init__(self, master):
		Frame.__init__(self,master)
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
		R1Q1.select()
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
		R1Q2.select()
		R2Q2 = Radiobutton(self,text="Seek out some pre-existing software that is similar and use that as an example", variable= self.varQ2, value=1)#(Reflector)
		R2Q2.grid(row=12, column= 2, sticky=W, padx=100)
		R3Q2 = Radiobutton(self, text="Get into a team / group and collectively solve the problem together", variable= self.varQ2, value=3)#(Theorist)
		R3Q2.grid(row=13, column= 2, sticky=W, padx=100)
		R4Q2 = Radiobutton(self, text="Solving the problem over a period of time in small sections", variable= self.varQ2, value=2)#(Pragmatist)
		R4Q2.grid(row=14, column= 2, sticky=W, padx=100)

		Q3 = Label(self,text="As a team you are about to start a software project for your new module and you need to \ncome up with a proper computer language which you will use.In the team meeting you will:",font=("BOLD",13))
		Q3.grid(row=15, column=1, columnspan=4,sticky=W,padx=50,pady=10)

		self.varQ3 = IntVar()
		R1Q3 = Radiobutton(self, text="Start watching other team’s solutions on the problem to help you with your decision.", variable=self.varQ3, value=2)
		R1Q3.grid(row=16, column= 2, sticky=W, padx=100)
		R1Q3.select()
		R2Q3 = Radiobutton(self,text="Start a discussion about the language with your team members.", variable= self.varQ3, value=3)
		R2Q3.grid(row=17, column= 2, sticky=W, padx=100)
		R3Q3 = Radiobutton(self, text="Think more about the algorithms which will be needed in the project to get the most efficient language", variable= self.varQ3, value=4)
		R3Q3.grid(row=18, column= 2, sticky=W, padx=100)
		R4Q3 = Radiobutton(self, text="Research what the last year students had used and pick the language with the most successful projects.", variable= self.varQ3, value=1)
		R4Q3.grid(row=19, column= 2, sticky=W, padx=100)

		Q4 = Label(self,text="You have just received your first web applications coursework brief and you decide to start\n developing your website, you wanted to try positioning items in your website although you\n have not fully gone through it in class, you’re friends told you positioning items in the site \nis very hard, do you:",font=("BOLD",13))
		Q4.grid(row=20, column=1, columnspan=4,sticky=W,padx=50,pady=10)

		self.varQ4 = IntVar()
		R1Q4 = Radiobutton(self, text="Read about how you can position items online.", variable=self.varQ4, value=2)#(Pragmatist)
		R1Q4.grid(row=21, column= 2, sticky=W, padx=100)
		R1Q4.select()
		R2Q4 = Radiobutton(self,text="Keep on trying positioning items until you succeed.", variable= self.varQ4, value=4)#(Activist)
		R2Q4.grid(row=22, column= 2, sticky=W, padx=100)
		R3Q4 = Radiobutton(self, text="Read how positioning items works before you try doing it", variable= self.varQ4, value=3)#(Theorist)
		R3Q4.grid(row=23, column= 2, sticky=W, padx=100)
		R4Q4 = Radiobutton(self, text="Wait until you fully cover positioning in class and work on what you did in class", variable= self.varQ4, value=1)#(Reflector)
		R4Q4.grid(row=24, column= 2, sticky=W, padx=100)

		Q5 = Label(self,text="When learning new mathematical theory, do you prefer?",font=("BOLD",13))
		Q5.grid(row=25, column=1, columnspan=4,sticky=W,padx=50,pady=10)

		self.varQ5 = IntVar()
		R1Q4 = Radiobutton(self, text="Seeing the theory applied in the real world and seeing a purpose for it.", variable=self.varQ5, value=2)#(Pragmatist)
		R1Q4.grid(row=26, column= 2, sticky=W, padx=100)
		R1Q4.select()
		R2Q4 = Radiobutton(self,text="Get stuck in and start doing lots of practice exercise", variable= self.varQ5, value=4)#(Activist)
		R2Q4.grid(row=27, column= 2, sticky=W, padx=100)
		R3Q4 = Radiobutton(self, text="Learn the proof of the theory.", variable= self.varQ5, value=3)#(Theorist)
		R3Q4.grid(row=28, column= 2, sticky=W, padx=100)
		R4Q4 = Radiobutton(self, text="Watch someone go through examples and work it out in your head", variable= self.varQ5, value=1)#(Reflector)
		R4Q4.grid(row=29, column= 2, sticky=W, padx=100)

	def collectAnswers(self):
		radioAnswer1 = self.varQ1.get()
		radioAnswer2 = self.varQ2.get()
		radioAnswer3 = self.varQ3.get()
		radioAnswer4 = self.varQ4.get()
		radioAnswer5 = self.varQ5.get()
		Questionnaire.answerList.append(radioAnswer1)
		Questionnaire.answerList.append(radioAnswer2)
		Questionnaire.answerList.append(radioAnswer3)
		Questionnaire.answerList.append(radioAnswer4)
		Questionnaire.answerList.append(radioAnswer5)
		#print([radioAnswer1, radioAnswer2])
		#print(Questionnaire.answerList)
		#stops the button from being accessed by the user
		self.btn.configure(state=DISABLED, text="Finished")
		print(Questionnaire.answerList)
		CalResults(Questionnaire.answerList,"H&M")
		
	def getAnswers(self):
		return Questionnaire.answerList

	def quitQues(self):
		tkinter.messagebox.showinfo("Warning", "You are going to quit the questionnaire")
		quit()
	
	def createButton(self):
		self.btn = Button(self, text="Submit",command=self.collectAnswers)
		self.btn.grid(row=30, column=2)

	def createQuit(self):
		self.quitBtn = Button(self, text="Quit", command=self.quitQues)
		self.quitBtn.grid(row=28, column=3)

def main():
	window = Tk()
	window.title('Questionnaire')
	window.resizable(0,0)
	application = Questionnaire(window)
	window.mainloop()

if __name__ == "__main__":
	main()
