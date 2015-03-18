from tkinter import *
numberForTest = [1,2,3,4,5]

class honeyMumford(Frame):
	results = []

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createQuestion()
		#	self.createButton()

	def createQuestion(self):
		self.varQ1 = IntVar
		self.question1 = Label(self,text="When Learning What an Object is in object orientated programming do you prefer :")
		self.question1.grid(row=1, column=1, columnspan=4,sticky=W,padx=50,pady=10)

		#creating question1 answers
		self.varQ1 = IntVar()
		self.R1Q1 = Radiobutton(self, text="To role-play a scenario", variable=self.varQ1, value=4)#(Activist)
		self.R1Q1.grid(row=2, column= 2, sticky=W, padx=100)
		self.R1Q1.select()
		self.R2Q1 = Radiobutton(self,text="Read a book about the subject", variable= self.varQ1, value=3) #(Theorist)
		self.R2Q1.grid(row=3, column= 2, sticky=W, padx=100)
		self.R3Q1 = Radiobutton(self, text="Be given a relevant case study that applies in a working environment", variable= self.varQ1, value=2) #(Pragmatist)
		self.R3Q1.grid(row=4, column= 2, sticky=W, padx=100)
		self.R4Q1 = Radiobutton(self, text="Discuss in a group", variable= self.varQ1, value=1) #(Reflector)
		self.R4Q1.grid(row=5, column= 2, sticky=W, padx=100)

	def getResults(self):
		return honeyMumford.results
	
	def createButton(self):
		self.number = 2
		self.nextQuestion = Button(self, text="Next Question", command= lambda: self.changeQuestion(self.number))
		self.nextQuestion.grid(row=6, column=2)

	def changeQuestion(self, number):
		answer = self.varQ1.get()
		honeyMumford.results.append(answer)
		if number == 2:
			self.question1["text"] = "When given a task to develop a piece of software for an item of coursework, do you find it best to:"
			self.R1Q1["text"] = "Go straight into the problem with confidence of solving it"
			self.R1Q1["value"] = 4 #(Activist)
			self.R2Q1["text"] = "Seek out some pre-existing software that is similar and use that as an example"
			self.R2Q1["value"] = 1 #(Theorist)
			self.R3Q1["text"] = "Get into a team / group and collectively solve the problem together"
			self.R3Q1["value"] = 3 #(Pragmatist)
			self.R4Q1["text"] = "Solving the problem over a period of time in small sections"
			self.R4Q1["value"] = 2 #(Reflector)
			self.number = 3
		elif number == 3:
			self.question1["text"] = "As a team you are about to start a software project for your new module and you need to \ncome up with a proper computer language which you will use.In the team meeting you will:"
			self.R1Q1["text"] = "Start a discussion about the language with your team members"
			self.R1Q1["value"] = 3 
			self.R2Q1["text"] = "Start watching other team’s solutions on the problem to help you with your decision" 
			self.R2Q1["value"] = 2
			self.R3Q1["text"] = "Think more about the algorithms which will be needed in the project to get the most efficient language"
			self.R3Q1["value"] = 4
			self.R4Q1["text"] = "Research what the last year students had used and pick the language with the most successful projects"
			self.R4Q1["value"] = 1
			self.number = 4
		elif number == 4:
			self.question1["text"] = "As a team you are about to start a software project for your new module and you need to \ncome up with a proper computer language which you will use.In the team meeting you will:"
			self.R1Q1["text"] = "Wait until you fully cover positioning in class and work on what you did in class later"
			self.R1Q1["value"] = 1
			self.R2Q1["text"] = "Keep on trying positioning items until you succeed"
			self.R2Q1["value"] = 3 
			self.R3Q1["text"] = "Read how positioning items works before you try doing it"
			self.R3Q1["value"] = 4
			self.R4Q1["text"] = "Read about how you can position items online"
			self.R4Q1["value"] = 2 
			self.number = 5
		elif number == 5:
			self.question1["text"] = "When learning new mathematical theory, do you prefer:"
			self.R1Q1["text"] = "Seeing the theory applied in the real world and seeing a purpose for it."
			self.R1Q1["value"] = 2
			self.R2Q1["text"] = "Get stuck in and start doing lots of practice exercise"
			self.R2Q1["value"] = 4
			self.R3Q1["text"] = "Learn the proof of the theory"
			self.R3Q1["value"] = 3
			self.R4Q1["text"] = "Watch someone go through examples and work it out in your head"
			self.R4Q1["value"] = 1
			self.number = 6	
		elif number == 6:
			return True

##### test code ######

def test_button(app):
	try:
		removedNumber = numberForTest.pop(0)
		app.changeQuestion(removedNumber)
		seeCurrentResult = app.getResults()
		print(seeCurrentResult)
	except IndexError:
		print("Test Complete")

def main():
	root = Tk()
	app = honeyMumford(root)
	app.pack(side = TOP, padx =20, pady =20)
	btn = Button( root , text = 'Next Question', command = lambda: test_button(app))
	btn.pack(side = BOTTOM, padx =20, pady =20)
	root.mainloop()

if __name__ == "__main__":
	main()