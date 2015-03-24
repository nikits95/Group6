from tkinter import *
import tkinter.messagebox
numberForTest = [1,2,3,4,5]

class VARKQ(Frame):
	results = []

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createQuestion()
		self.createQuitButton()

	def createQuitButton(self):
		btnQuit = Button(self, text="Quit", command=self.stopQuestionnaire)
		btnQuit.pack(side=BOTTOM)

	def stopQuestionnaire(self):
		if tkinter.messagebox.askyesno("You are about to quit!", "Are you sure you want to quit?", icon="warning"):
			quit()
		else:
			pass

	def createQuestion(self): #1 =Visu 2=Kinesthetic 3=Aural 4=Reading
		self.varQ1 = IntVar
		self.question1 = Label(self,text="When using a brand new IDE or any other software to allow coding, do you understand it by:")
		self.question1.pack(side=TOP, anchor=W, padx=20, pady=20)

		#creating question1 answers
		self.varQ1 = IntVar()
		self.R1Q1 = Radiobutton(self, text="Watching a video tutorial online to understand how it works.", variable=self.varQ1, value=1)#(visual)
		self.R1Q1.pack(anchor=W)
		self.R1Q1.select()
		self.R2Q1 = Radiobutton(self,text="Play with the software and overtime learn how to use it", variable= self.varQ1, value=2) #(Kinesthetic)
		self.R2Q1.pack(anchor=W)
		self.R3Q1 = Radiobutton(self, text="Ask someone who has had experience with the software", variable= self.varQ1, value=3) #(Aural)
		self.R3Q1.pack(anchor=W)
		self.R4Q1 = Radiobutton(self, text="Find an online or locally saved manual to learn the software", variable= self.varQ1, value=4) #(Reading)
		self.R4Q1.pack(anchor=W)

	def getResults(self):
		return VARKQ.results

	def changeQuestion(self, number):
		answer = self.varQ1.get()
		VARKQ.results.append(answer)
		if number == 2:
			self.question1["text"] = "When going through how a website works with a Web server do you prefer to:"
			self.R1Q1["text"] = "Talk about it in a group"
			self.R1Q1["value"] = 3 #(Aural)
			self.R2Q1["text"] = "Read through lecturer notes"
			self.R2Q1["value"] = 4 #(Reading)
			self.R3Q1["text"] = "See a Diagram "
			self.R3Q1["value"] = 1 #(Visual)
			self.R4Q1["text"] = "Build a website and host it on a web server"
			self.R4Q1["value"] = 2#(Kinesthetic)
			self.number = 3
		elif number == 3:
			self.question1["text"] = "You are about to use a function from a new framework, you are unsure how it works. You will:"
			self.R1Q1["text"] = "Read the documentation given in the website of the framework"
			self.R1Q1["value"] = 4 
			self.R2Q1["text"] = "Check examples already done by somebody" 
			self.R2Q1["value"] = 1
			self.R3Q1["text"] = "Call and ask a friend who has experience with this framework"
			self.R3Q1["value"] = 3
			self.R4Q1["text"] = "Try to figure out how it works by trial and error"
			self.R4Q1["value"] = 2
			self.number = 4
		elif number == 4:
			self.question1["text"] = "You are revising networking, you see the different network topologies (e.g. Bus). Do you:"
			self.R1Q1["text"] = "Go to the nearest computer lab and try to analyse which topology the lab is using."
			self.R1Q1["value"] = 2
			self.R2Q1["text"] = "I understood the topologies after I attended the lecture."
			self.R2Q1["value"] = 3 
			self.R3Q1["text"] = "Go over your notes from the lecture (the notes consist of bullet points)"
			self.R3Q1["value"] = 4
			self.R4Q1["text"] = "Look at diagrams based on the topologies and learn from there"
			self.R4Q1["value"] = 1 
			self.number = 5
		elif number == 5:
			self.question1["text"] = "You are helping someone with a programming problem, to answer them would you:"
			self.R1Q1["text"] = "Write down Pseudocode/code to help them solve the problem. "
			self.R1Q1["value"] = 4
			self.R2Q1["text"] = "Go through the problem on the computers with the person"
			self.R2Q1["value"] = 2
			self.R3Q1["text"] = "Explain how to solve the problem with diagrams and arrows."
			self.R3Q1["value"] = 1
			self.R4Q1["text"] = "Tell the person how to solve the problem."
			self.R4Q1["value"] = 3
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
	app = VARKQ(root)
	app.pack(side = TOP, padx =20, pady =20)
	btn = Button( root , text = 'Next Question', command = lambda: test_button(app))
	btn.pack(side = BOTTOM, padx =20, pady =20)
	root.mainloop()

if __name__ == "__main__":
	main()