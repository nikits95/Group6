from tkinter import *

class Home(Frame):
  def __init__(self,master):
    Frame.__init__(self,master)
    alable = Label(self,text="Home")
    alable.grid(row=1, column=1)
    self.create_degree_program()
    self.create_yearOfStudy()
    self.createButton()


  def get_information(self):
    #return "Tim","BIS"
    return str(self.varYear.get()), str(self.listProg.get(self.listProg.curselection()))

  def create_degree_program(self):
    lblDegree = Label(self, text="Degree Program")
    lblDegree.grid(row=3, column=0, sticky=NE)

    self.listProg = Listbox(self, height= 3)
    scroll = Scrollbar(self, command= self.listProg.yview) 
    self.listProg.configure(yscrollcommand=scroll.set)
    self.listProg.grid(row=3, column=1, sticky=NE, rowspan=3) 
    scroll.grid(row=3, column=4, sticky=W)
    
    for item in ["CS", "CS with", "BIS", "SE", "Joints"]: 
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

  def createButton(self):
    btn = Button(self, text="Submit", command=self.get_information)
    btn.grid(row=12)

##### Test code

def test_button(f):
    (a,b) = f.get_information()
    print(a,b)

def main():
  window = Tk()
  f1 = Information(window)
  f1.pack(side = TOP, padx =20, pady =20)
  btn = Button( window , text = 'Choose',
    command = lambda: test_button(f1))
  btn.pack(side = BOTTOM, padx =20, pady =20)
  window.mainloop()

if __name__ == '__main__':
  main()
