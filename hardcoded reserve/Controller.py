from tkinter import *
from home import *
from honeyMumford import *
from CalResults import *
from displayStyle import *
from VARKQ import *
from storage import *
from admin import *
from chartGenerator import *
import tkinter.messagebox

class Controller(Frame):

	learningTypeStoreage = []
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master

		self.cont_frame = Frame(self.root)
		self.cont_frame.pack(side=TOP)
		self.root.geometry("800x500")

		self.homepage = Home(self.cont_frame)
		self.homepage.pack()

		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(self.homepage))
		self.btnHome.pack(side=BOTTOM)

		self.btnLec = Button(self.cont_frame, text="lecturer Area", command= self.lecturePage)
		self.btnLec.pack(side=BOTTOM)

	def lecturePage(self):
		if tkinter.messagebox.askyesno("Are you lecturer at COMSC", "Are you a member of the COMSC Staff?", icon="warning"):
			self.homepage.destroy()
			self.btnLec["command"] = self.goback
			self.btnLec["text"] = "Go Back"
			self.btnMoreGraphical = Button(self.cont_frame, text="Overall Results Graph", command=self.makeGraph)
			self.btnMoreGraphical.pack(side=BOTTOM)

			self.adminPage = admin(self.cont_frame)
			self.adminPage.pack()
			self.btnHome.destroy()
			self.update()
		else:
			pass

	def makeGraph(self):
		self.btnLec.destroy()
		self.adminPage.destroy()
		self.btnMoreGraphical["command"] = self.returnAnalysis
		self.btnMoreGraphical["text"] = "Back to analysis"
		self.graphInter = mygui(self.cont_frame)
		self.graphInter.pack()
		self.update()

	def returnAnalysis(self):
		self.graphInter.stopGraph()
		self.graphInter.destroy()
		self.btnMoreGraphical["command"] = self.makeGraph
		self.btnMoreGraphical["text"] = "Overall Results Graph"
		self.btnLec = Button(self.cont_frame, text="Go back", command= self.goback)
		self.btnLec.pack(side=BOTTOM)
		
		self.adminPage = admin(self.cont_frame)
		self.adminPage.pack()
		self.update()


	def goback(self):
		self.adminPage.destroy()
		self.btnLec["command"] = self.lecturePage
		self.btnLec["text"] = "lecturer Area"
		self.btnMoreGraphical.destroy()
		self.homepage = Home(self.cont_frame)
		self.homepage.pack()
		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(self.homepage))
		self.btnHome.pack(side=BOTTOM)
		self.update()

	def gettingHomeData(self, currentframe):
		try:
			self.btnLec.destroy()
			(self.studentNumber,self.yearOfStudy,self.degreeProgram) = currentframe.get_information()
			currentframe.destroy()

			honeyMumfordQuestionnaire = honeyMumford(self.cont_frame)
			self.root.geometry("800x300")
			honeyMumfordQuestionnaire.pack()

			self.number = 2
			self.btnHome["text"] = "Next" 
			self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, honeyMumfordQuestionnaire,"Honey & Mumford",1)
		except TypeError:
			pass
			
	def changeCurrentQuestion(self,number, selectedFrame, questionnaireType, numberCompleted):
		if number in range(1,8):
			if number == 2:
				selectedFrame.changeQuestion(2)
				self.number +=1
			elif number == 3:
				selectedFrame.changeQuestion(3)
				self.number +=1
			elif number == 4:
				selectedFrame.changeQuestion(4)
				self.number +=1
			elif number == 5:
				selectedFrame.changeQuestion(5)
				self.number +=1
			elif number == 6:
				selectedFrame.changeQuestion(6)
				self.number +=1

				self.frameResults = selectedFrame.getResults()
				self.update()
				
				selectedFrame.destroy()
				#print(self.frameResults)
				self.questionnaireResults = CalResults(self.frameResults, questionnaireType)
				selectedFrame.clearResults()
				self.gettingInformation(self.questionnaireResults, questionnaireType,numberCompleted)

	def gettingInformation(self,curretnFrame, questionnaireType, completedQuestionnaire):
		self.learningType = curretnFrame.getType()
		Controller.learningTypeStoreage.append(self.learningType)
		self.results = displayStyle(self.cont_frame, self.learningType, questionnaireType)
		self.results.pack()

		if completedQuestionnaire == 1:
			self.btnHome["text"] = "VARK Questionnaire"
			self.btnHome["command"] = lambda: self.nextQuestionnaire()
		else:
			self.btnHome["text"] = "Exit"
			self.btnHome["command"] = lambda: self.sendHome()
			storingInfo = storage()
			storingInfo.add_data(self.studentNumber,self.degreeProgram, self.yearOfStudy, Controller.learningTypeStoreage[0], Controller.learningTypeStoreage[1])
		self.update()

	def nextQuestionnaire(self):
		self.results.destroy()
		self.btnHome["text"] = "Next"
		self.number = 2
		self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, varkQues,"VARK",2)
		varkQues = VARKQ(self.cont_frame)
		varkQues.pack()

	def sendHome(self):
		self.results.destroy()
		self.homepage = Home(self.cont_frame)
		self.homepage.pack()
		Controller.learningTypeStoreage = []
		self.root.geometry("800x500")
		self.btnHome["text"] = "Submit"
		self.btnHome["command"] = lambda: self.gettingHomeData(self.homepage)
		self.btnLec = Button(self.cont_frame, text="lecturer Area", command= self.lecturePage)
		self.btnLec.pack(side=BOTTOM)
		self.update()
		
def main():
	root = Tk()
	root.title("Questionnaire")
	app = Controller(root)
	root.mainloop()

if __name__ == "__main__":
	main()
