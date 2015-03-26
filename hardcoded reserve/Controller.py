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

	learningTypeStoreage = [] #list will store the answers for each leanring style
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master

		self.cont_frame = Frame(self.root) #main frame that other frames will be attached too
		self.cont_frame.pack(side=TOP)
		self.root.geometry("800x600")

		self.homepage = Home(self.cont_frame)
		self.homepage.pack()

		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(self.homepage))
		self.btnHome.pack(side=BOTTOM)

		self.btnLec = Button(self.cont_frame, text="lecturer Area", command= self.lecturePage)
		self.btnLec.pack(side=BOTTOM)

	def lecturePage(self):
		""" This method will ask a yes or no message box to the user and depending on the results will 
		affect what is displayed on screen. If yes is selected then the admin menu will be displayed
		otherwise it will just leave the user of the home screen.
		"""
		if tkinter.messagebox.askyesno("Are you lecturer at COMSC", "Are you a member of the COMSC Staff?", icon="warning"):
			self.homepage.destroy()
			self.btnLec["command"] = self.goback
			self.btnLec["text"] = "Go Back"
			#make 3 buttons and place them on frame
			self.btnMoreGraphical = Button(self.cont_frame, text="Overall Results Graph", command= lambda: self.makeGraph(0))
			self.btnMoreGraphical.pack(side=BOTTOM)

			self.btnMoreGraphicalVARK = Button(self.cont_frame, text="VARK Results Graph", command=lambda: self.makeGraph(1))
			self.btnMoreGraphicalVARK.pack(side=BOTTOM)

			self.btnMoreGraphicalHoney = Button(self.cont_frame, text="H & M Results Graph", command=lambda: self.makeGraph(2))
			self.btnMoreGraphicalHoney.pack(side=BOTTOM)

			#create admin page
			self.adminPage = admin(self.cont_frame)
			self.adminPage.pack()
			#destroy home page
			self.btnHome.destroy()
			self.update()
		else:
			#if no then do nothing
			pass

	def makeGraph(self, number):
		"""This method is used with the admin page. Upon one of the three buttons from the above function 
		being pressed by the user, it will generate and load up a graph of the results from the questionnaire
		"""
		self.btnLec.destroy() 
		self.adminPage.destroy() #destroy the admiin page
		self.btnMoreGraphical["command"] = self.returnAnalysis #configure button to be used on screen
		self.btnMoreGraphical["text"] = "Back to analysis"
		#destroy buttons that are not needed
		self.btnMoreGraphicalVARK.destroy() 
		self.btnMoreGraphicalHoney.destroy()
		#create graph and pass values 0 overall results, 1 for VARK and 2 for H&M
		self.graphInter = mygui(self.cont_frame, number)
		self.graphInter.pack()
		self.update()

	def returnAnalysis(self):
		"""This method is used after the makeGraph method. Upon pressing the go back button that 
		was configured above. It will make the changes to bring the user back to the admin page
		"""

		self.graphInter.stopGraph() #destory the current graph
		self.graphInter.destroy() #destroy the frame the graph was in 
		self.btnMoreGraphical.destroy()
		#make 3 buttons for the admin page to then allow access back to the graph
		self.btnMoreGraphical = Button(self.cont_frame, text="Overall Results Graph", command= lambda: self.makeGraph(0))
		self.btnMoreGraphical.pack(side=BOTTOM)

		self.btnMoreGraphicalVARK = Button(self.cont_frame, text="VARK Results Graph", command=lambda: self.makeGraph(1))
		self.btnMoreGraphicalVARK.pack(side=BOTTOM)

		self.btnMoreGraphicalHoney = Button(self.cont_frame, text="H & M Results Graph", command=lambda: self.makeGraph(2))
		self.btnMoreGraphicalHoney.pack(side=BOTTOM)
		
		#make another button that will allow the user to reutrn to the hoem back
		self.btnLec = Button(self.cont_frame, text="Go back", command= self.goback)
		self.btnLec.pack(side=BOTTOM)
		
		#create the admin page
		self.adminPage = admin(self.cont_frame)
		self.adminPage.pack()
		self.update()


	def goback(self):
		"""
		Thsi method will destroy all the admin page buttons and then change certian buttons that 
		will allow access to the Questionnaire and to the admin page again. It will then create the 
		home page again
		"""
		self.adminPage.destroy() #destroy the admin page
		#destroy undeed buttons
		self.btnMoreGraphicalHoney.destroy()
		self.btnMoreGraphicalVARK.destroy()
		#configure buttons to be used
		self.btnLec["command"] = self.lecturePage
		self.btnLec["text"] = "lecturer Area"
		self.btnMoreGraphical.destroy()
		#create the buttons and home page itself
		self.homepage = Home(self.cont_frame)
		self.homepage.pack()
		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(self.homepage))
		self.btnHome.pack(side=BOTTOM)
		self.update()

	def gettingHomeData(self, currentframe):
		"""This method is the one that starts the questionnaire. An exception is used to prevent a expcetion being raised
		when the user enters a invalid number. This prevents the system from crashing. If the exception is not raised it will
		begin the Questionnaire.
		"""
		try:
			self.btnLec.destroy() #destroy undeed buttons
			(self.studentNumber,self.yearOfStudy,self.degreeProgram) = currentframe.get_information() 
			#on the current frame, use methood get_inforamtion() to return the students input details
			currentframe.destroy() #destroy the frame 

			#create 
			honeyMumfordQuestionnaire = honeyMumford(self.cont_frame)
			self.root.geometry("800x300")
			honeyMumfordQuestionnaire.pack()

			self.number = 2 #questionnaire pointer set to 2, used in changeCurrentQuestion method
			#set buttons 
			self.btnHome["text"] = "Next" 
			self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, honeyMumfordQuestionnaire,"Honey & Mumford",1)
		except TypeError:
			#on exception do nothing, home.py will provide a message box to inform the user
			pass
			
	def changeCurrentQuestion(self,number, selectedFrame, questionnaireType, numberCompleted):
		"""This method will moniter and modify the questions for each questionnaire, then pass them to 
		be calculated. It will use a pointer that will go into the questionnaire classes to then change all the
		questions, answers and values.
		"""
		if number in range(1,8):
			#depending which number is in the pointer, the method will go into selectedFrame and make the question change 
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

				self.frameResults = selectedFrame.getResults() #get the results from the getResults method
				self.update()
				
				selectedFrame.destroy() #destroy the frame
				self.questionnaireResults = CalResults(self.frameResults, questionnaireType) #pass the results of the questionnaure ot the CalResults class
				#clear all the data inside the questionnaire class
				selectedFrame.clearResults()
				#call gettingInformation method
				self.gettingInformation(self.questionnaireResults, questionnaireType,numberCompleted)

	def gettingInformation(self,currentFrame, questionnaireType, completedQuestionnaire):
		"""This method will display the reslts of each questionnaire after the user has completed each one
		This will be shown instantly to the user. If the completedQuestionnaire is 1 then load next Questionnaire
		otherwise display the exit button which goes back to the start.
		"""

		self.learningType = currentFrame.getType()
		#add the value from the questionnaire to class list
		Controller.learningTypeStoreage.append(self.learningType)
		#call the displayStyle and will then display to screen the stduent's results
		self.results = displayStyle(self.cont_frame, self.learningType, questionnaireType)
		self.results.pack()

		#if completedQuestionnaire equals 1 then configure button to load next questionnaire
		if completedQuestionnaire == 1:
			self.btnHome["text"] = "VARK Questionnaire"
			self.btnHome["command"] = lambda: self.nextQuestionnaire()
		else:
			#otherwise configue the buttons to take the user back to the home page
			self.btnHome["text"] = "Exit"
			self.btnHome["command"] = lambda: self.sendHome()
			storingInfo = storage() #define class to then save the student's inforamtion
			#pass all the inforamtion from the system to the .dat file via add_data method from storage.py
			storingInfo.add_data(self.studentNumber,self.degreeProgram, self.yearOfStudy, Controller.learningTypeStoreage[0], Controller.learningTypeStoreage[1])
		self.update()

	def nextQuestionnaire(self):
		"""This method will load the final questionnaire for the user. It will destroy the results frame and then
		configute the buttons to allow the controller to set each question up.
		"""
		self.results.destroy()# destroy frame
		#configure buttons
		self.btnHome["text"] = "Next"
		self.number = 2 #set question pointer = 2
		self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, varkQues,"VARK",2)
		varkQues = VARKQ(self.cont_frame) #load the VARK questionnaire
		varkQues.pack()

	def sendHome(self):
		"""This method will reset the entire questionnaire so it can be then reused by another student
		It will reset everything and make all the buttons needed. Along with destorying the current frame.
		"""
		self.results.destroy() #destroy the current frame in use
		#load and pack the home page
		self.homepage = Home(self.cont_frame)
		self.homepage.pack()
		Controller.learningTypeStoreage = [] #clear the class list, so can be reused.
		self.root.geometry("800x600")
		#configure te buttons to be used on the home page
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