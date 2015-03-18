from tkinter import *
from Home import *
from honeyMumford import *
from CalResults import *
from displayStyle import *
from VARKQ import *

class Controller(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master

		self.cont_frame = Frame(self.root)
		self.cont_frame.pack(side=TOP, padx=5, pady=5)

		homepage = Home(self.cont_frame)
		homepage.pack()

		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(homepage))
		self.btnHome.pack(side=BOTTOM)

	def gettingHomeData(self, currentframe):
		(yearOfStudy,degreeProgram) = currentframe.get_information()
		currentframe.destroy()

		honeyMumfordQuestionnaire = honeyMumford(self.cont_frame)
		honeyMumfordQuestionnaire.pack()

		self.number = 2
		self.btnHome["text"] = "Submit" 
		self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, honeyMumfordQuestionnaire,"Honey & Mumford",1)

	def changeCurrentQuestion(self,number, selectedframe, questionnaireType, numberCompleted):
		if number in range(1,8):
			if number == 2:
				a = selectedframe.changeQuestion(2)
				self.number +=1
			elif number == 3:
				selectedframe.changeQuestion(3)
				self.number +=1
			elif number == 4:
				selectedframe.changeQuestion(4)
				self.number +=1
			elif number == 5:
				selectedframe.changeQuestion(5)
				self.number +=1
			elif number == 6:
				selectedframe.changeQuestion(6)
				self.number +=1

				self.honeyResults = selectedframe.getResults()
				self.update()
				#print(self.honeyResults)
				selectedframe.destroy()
				
				self.questionnaireResults = CalResults(self.honeyResults, questionnaireType)
				self.gettingInformation(self.questionnaireResults, questionnaireType,numberCompleted)

	def gettingInformation(self,curretnFrame, questionnaireType, completedQuestionnaire):
		learningType = curretnFrame.getType()
		#print(learningType)
		self.results = displayStyle(self.cont_frame, learningType, questionnaireType)
		self.results.pack()

		if completedQuestionnaire == 1:
			self.btnHome["text"] = "VARK Questionnaire"
			self.btnHome["command"] = lambda: self.nextQuestionnaire()
		else:
			self.btnHome["text"] = "Exit"
			self.btnHome["command"] = lambda: self.sendHome()
		self.update()

	def nextQuestionnaire(self):
		self.results.destroy()
		self.btnHome["text"] = "Submit"
		self.number = 2
		self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, varkQues,"VARK",2)
		varkQues = VARKQ(self.cont_frame)
		varkQues.pack()

	def sendHome(self):
		self.results.destroy()
		homepage = Home(self.cont_frame)
		homepage.pack(side=LEFT, padx=20, pady=20)
		self.btnHome["text"] = "Submit"
		self.btnHome["command"] = lambda: self.gettingHomeData(homepage)
		self.quit()
		self.update()
		


		
def main():
	root = Tk()
	root.title("Questionnaire")
	app = Controller(root)
	root.mainloop()

if __name__ == "__main__":
	main()