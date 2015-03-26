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
	#list to hold the learning type inforamtion
	learningTypeStoreage = []
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master
		
		#creates the main frame that will be used in each frame
		self.cont_frame = Frame(self.root)
		self.cont_frame.pack(side=TOP)
		self.root.geometry("800x500")
	
		#home.py is called
		self.homepage = Home(self.cont_frame)
		self.homepage.pack()
		
		#creates the buttons for the system
		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(self.homepage))
		self.btnHome.pack(side=BOTTOM)

		self.btnLec = Button(self.cont_frame, text="lecturer Area", command= self.lecturePage)
		self.btnLec.pack(side=BOTTOM)

	def lecturePage(self):
		#lecture messagebox which askes yes or ni
		if tkinter.messagebox.askyesno("Are you lecturer at COMSC", "Are you a member of the COMSC Staff?", icon="warning"):
			#if yes destory the home page
			self.homepage.destroy()
			self.btnLec["command"] = self.goback #configure the buttons for reuse
			self.btnLec["text"] = "Go Back"
			self.btnMoreGraphical = Button(self.cont_frame, text="Overall Results Graph", command=self.makeGraph)
			self.btnMoreGraphical.pack(side=BOTTOM) #create a new button for the lecturer

			self.adminPage = admin(self.cont_frame)
			#create the admin page from admin.py
			self.adminPage.pack()
			self.btnHome.destroy() #destory the home button
			self.update()
		else:
			#if no do nothing
			pass

	def makeGraph(self):
		#loads the graph and destroys button that are no needed
		self.btnLec.destroy()
		self.adminPage.destroy()
		self.btnMoreGraphical["command"] = self.returnAnalysis #re-configure button to go back pages
		self.btnMoreGraphical["text"] = "Back to analysis"
		self.graphInter = mygui(self.cont_frame)
		#load image
		self.graphInter.pack()
		self.update()

	def returnAnalysis(self):
		self.graphInter.stopGraph() #destroys the graph
		self.graphInter.destroy() #destroys the graph frame
		self.btnMoreGraphical["command"] = self.makeGraph #re - configure buttons
		self.btnMoreGraphical["text"] = "Overall Results Graph"
		self.btnLec = Button(self.cont_frame, text="Go back", command= self.goback)
		self.btnLec.pack(side=BOTTOM)
		
		self.adminPage = admin(self.cont_frame) #created admin frame
		self.adminPage.pack()
		self.update()


	def goback(self):
		#function allows the user to go back from teh admin page
		self.adminPage.destroy()
		self.btnLec["command"] = self.lecturePage #re-configure the buttons
		self.btnLec["text"] = "lecturer Area"
		self.btnMoreGraphical.destroy() #destroy the frame in use
		self.homepage = Home(self.cont_frame) #make Home frame
		self.homepage.pack()
		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(self.homepage))
		self.btnHome.pack(side=BOTTOM) #create buttons needed for the frame
		self.update()

	def gettingHomeData(self, currentframe):
		#frame gets informtion from te student as they submit data
		try:
		#Exception used to handle any form of non-numerical data input
			self.btnLec.destroy()
			(self.studentNumber,self.yearOfStudy,self.degreeProgram) = currentframe.get_information() #get the informtion from the current frame via get_inforamton method
			currentframe.destroy() #destroy the current frame

			honeyMumfordQuestionnaire = honeyMumford(self.cont_frame) #load up the first questionnaire
			self.root.geometry("800x300") 
			honeyMumfordQuestionnaire.pack()

			self.number = 2 # this number is used to identify what question needs to be loaded
			self.btnHome["text"] = "Next" #configure button
			self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, honeyMumfordQuestionnaire,"Honey & Mumford",1)
		except TypeError:
			#if letter do nothing as home.py has message box that informs the user
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
		#This function is only used to change the questionnaire
		self.results.destroy()
		self.btnHome["text"] = "Next" #configure buttons
		self.number = 2 #set the pointer for the number of clicks to 2
		self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, varkQues,"VARK",2)
		varkQues = VARKQ(self.cont_frame) #create the last questionnaire
		varkQues.pack()

	def sendHome(self):
		# This function resets the questionnaire so it can be re-taken
		self.results.destroy() #destroy current frame
		self.homepage = Home(self.cont_frame)
		self.homepage.pack() #create home frame
		Controller.learningTypeStoreage = [] #clear the list for re-use
		self.root.geometry("800x500")
		self.btnHome["text"] = "Submit" #configure buttons
		self.btnHome["command"] = lambda: self.gettingHomeData(self.homepage)
		self.btnLec = Button(self.cont_frame, text="lecturer Area", command= self.lecturePage)
		self.btnLec.pack(side=BOTTOM) #create buttons
		self.update()
		
def main():
	root = Tk()
	root.title("Questionnaire")
	app = Controller(root)
	root.mainloop()

if __name__ == "__main__":
	main()
