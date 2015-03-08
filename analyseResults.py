from tkinter import *

class analyseResults(Frame):

	def _init__(self,master):
		Frame.__init_(self,master)
		##call the methods for creating the Labels, buttons, etc here
		#e.g. self.createAnalyseButtons()

	def createAnalyseButtons(self):
		#creates the buttons need for the different types of results analysing
		#One needs to be by degree program, e.g all results for Computer Science
		#Another by year of study. e.g. first year

	def degreeProgramList(self,styleType):
		#style type will be provided by a drop down box
		#similar to the home menu, a list of the degree modules
		#That when clicked along with the button will pull information of a text file
		#then present what is the most common learning style, etc.

	def yearStudyList(self,styleType):
		#style type will be provided by a drop down box
		#same idea as above except has the year of study.

	def learningStyleType(self):
		#creates a drop down box that will return
		#either H&M or VARK Style for the above methods.

	def createAnalyseLabels(self):
		#creates the labels needed to expalin what each buttons do

	#add more methods if needed.




