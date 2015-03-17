from tkinter import *

class Home(Frame):
  def __init__(self,master):
    Frame.__init__(self,master)
    alable = Label(self,text="Information")
    alable.grid(row=1, column=1)
    self.grid()
    self.create_degree_program()
    self.create_yearOfStudy()
    self.create_button()

  def get_information(self):
    #return str(self.varYear.get()), str(self.listProg.get(self.listProg.curselection()))
    print(str(self.varYear.get()), str(self.listProg.get(self.listProg.curselection())))
    Home.grid_forget(self)

  def create_degree_program(self):
    #creates a label to go with the listbox
    lblDegree = Label(self, text="Degree Program")
    lblDegree.grid(row=3, column=0, sticky=NE)
    
    #creates a Listbox with a scrollbar to allow the student to select a degree
    self.listProg = Listbox(self, height= 3)
    scroll = Scrollbar(self, command= self.listProg.yview) 
    self.listProg.configure(yscrollcommand=scroll.set)
    self.listProg.grid(row=3, column=1, sticky=NE, rowspan=3) 
    scroll.grid(row=3, column=4, sticky=W)
    emptyLabel = Label(self) #used to make a break between listboxes
    emptyLabel.grid(row=6,column=1)

    
    #runs through a for loop of the different options that the student can pick
    for item in ["CS", "CS with", "BIS", "SE", "Joints",""]: 
      self.listProg.insert(END, item)
    self.listProg.selection_set(END)

  def create_yearOfStudy(self):
    lblYear = Label(self, text="Current Year of Study")
    lblYear.grid(row=8, column=0, sticky=NE)

    self.varYear = StringVar()
    R1 = Radiobutton(self, text="Year1", variable=self.varYear, value="Year1")
    R1.grid(row=8, column= 1, sticky=W, padx=100)
    R1.select()
    R2 = Radiobutton(self,text="Year2", variable= self.varYear, value="Year2")
    R2.grid(row=9, column= 1, sticky=W, padx=100)
    R3 = Radiobutton(self, text="Year3", variable= self.varYear, value="Year3") 
    R3.grid(row=10, column= 1, sticky=W, padx=100)
    R4 = Radiobutton(self, text="Year4", variable= self.varYear, value="Year4") 
    R4.grid(row=11, column= 1, sticky=W, padx=100)

  def create_button(self):
    btn = Button(self, text="Start Questionnaire", command=self.get_information)
    btn.grid(row=12, column=1)

def main():
  window = Tk()
  app = Home(window)
  window.mainloop()

if __name__ == '__main__':
  main()
