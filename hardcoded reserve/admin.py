from tkinter import *
from storage import *
import tkinter.messagebox



class admin(Frame):
  def __init__(self,master):
    Frame.__init__(self,master)
    alable = Label(self,text="Lecturer")
    alable.pack()
    self.create_degree_program()
    self.create_yearOfStudy()
    self.createVARKButton()
    self.createHMButton()
    self.createALLButton()

  def create_degree_program(self):
    lblDegree = Label(self, text="Select student degree:")
    lblDegree.pack()

    self.varDegree = StringVar()
    #creates all the radiobuttons for degree type

    R1 = Radiobutton(self, text="CS", variable=self.varDegree, value="CS")
    R1.pack(side=TOP, anchor=W)
    R1.select()
    R2 = Radiobutton(self,text="CS With", variable= self.varDegree, value="CS With")
    R2.pack(side=TOP, anchor=W)
    R3 = Radiobutton(self, text="SE", variable= self.varDegree, value="SE") 
    R3.pack(side=TOP, anchor=W)
    R4 = Radiobutton(self, text="Joints", variable= self.varDegree, value="Joints") 
    R4.pack(side=TOP, anchor=W)
    R5 = Radiobutton(self, text="BIS", variable= self.varDegree, value="BIS") 
    R5.pack(side=TOP, anchor=W)
  
  def create_yearOfStudy(self):
    lblYear = Label(self, text="Select year of study:")
    lblYear.pack()

    self.varYear = StringVar()
    #creates all the radiobuttons for current year
    R1 = Radiobutton(self, text="Year1", variable=self.varYear, value="Year1")
    R1.pack(side=TOP, anchor=W)
    R1.select()
    R2 = Radiobutton(self,text="Year2", variable= self.varYear, value="Year2")
    R2.pack(side=TOP, anchor=W)
    R3 = Radiobutton(self, text="Year3", variable= self.varYear, value="Year3") 
    R3.pack(side=TOP, anchor=W)
    R4 = Radiobutton(self, text="Year4", variable= self.varYear, value="Year4") 
    R4.pack(side=TOP, anchor=W)


  #the follwing 3 methods will create buttons for the frame
  def createVARKButton(self):
    #this button takes the user options from above radiobuttons and provides feedback to the user via a messagebox
    btn = Button(self, text="Get VARK analysis", command= lambda: self.getVARKData(self.varYear.get(), self.varDegree.get()))
    btn.pack(side=BOTTOM, anchor=N, fill=X)

  def createHMButton(self):
    #this button takes the user options from above radiobuttons and provides feedback to the user via a messagebox
    btn = Button(self, text="Get Honey and Mumford analysis", command= lambda: self.getHMData(self.varYear.get(), self.varDegree.get()))
    btn.pack(side=BOTTOM, anchor=N, fill=X)
    lblInfo = Label(self,text="Please select a year and degree type and\n press one of the following buttons to show data:")
    lblInfo.pack(side=BOTTOM, anchor=N)

  def createALLButton(self):
    #this button when pressed will display all the results from the questionnares and give feedback
    btn = Button(self, text="Get analysis on everything", command= lambda: self.getALLData(self.varYear.get(), self.varDegree.get()))
    btn.pack(side=BOTTOM, anchor=N, fill=X)
    blInfo = Label(self,text="Please press this button to get all the\n information from all students")
    blInfo.pack(side=BOTTOM, anchor=N, ipadx=20)


  def getVARKData(self, year, degreeType):
    a = storage()
    a.print_out_vark(year, degreeType)


  def getHMData(self, year, degreeType):
    a = storage()
    a.print_out_HM(year, degreeType)

  def getALLData(self, year, degreeType):
    a = storage()
    a.print_out_ALL(year, degreeType)  

			
##### test code ######


def main():
  window = Tk()
  window.title("Lecturer Page")
  f1 = admin(window)
  f1.pack(side = TOP, padx =20, pady =20)
  window.mainloop()

if __name__ == '__main__':
  main()
