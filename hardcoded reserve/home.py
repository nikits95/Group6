from tkinter import *
import tkinter.messagebox

class Home(Frame):
  def __init__(self,master):
    Frame.__init__(self,master)
    alable = Label(self,text="Home")
    alable.grid(row=0, column=1)
    self.create_degree_program()
    self.create_yearOfStudy()
    self.get_number()


  def get_information(self):
    try:
      return int(self.userNumber.get()),str(self.varYear.get()), str(self.varDegree.get())
    except ValueError:
      tkinter.messagebox.showinfo("Invalid Number", "Please ensure student number is only numbers",icon="warning")

  def create_degree_program(self):
    lblDegree = Label(self, text="Degree Program:")
    lblDegree.grid(row=3, column=0)
  
    self.varDegree = StringVar()
    R1 = Radiobutton(self, text="CS", variable=self.varDegree, value="CS")
    R1.grid(row=3, column= 1, sticky=W, padx=100)
    R1.select()
    R2 = Radiobutton(self,text="CS With", variable= self.varDegree, value="CS With")
    R2.grid(row=4, column= 1, sticky=W, padx=100)
    R3 = Radiobutton(self, text="SE", variable= self.varDegree, value="SE") 
    R3.grid(row=5, column= 1, sticky=W, padx=100)
    R4 = Radiobutton(self, text="Joints", variable= self.varDegree, value="Joints") 
    R4.grid(row=6, column= 1, sticky=W, padx=100, columnspan=2)

  def create_yearOfStudy(self):
    lblYear = Label(self, text="Current Year of Study:")
    lblYear.grid(row=9, column=0, sticky=NE)

    self.varYear = StringVar()
    R1 = Radiobutton(self, text="Year1", variable=self.varYear, value="Year1")
    R1.grid(row=10, column= 1, sticky=W, padx=100)
    R1.select()
    R2 = Radiobutton(self,text="Year2", variable= self.varYear, value="Year2")
    R2.grid(row=11, column= 1, sticky=W, padx=100)
    R3 = Radiobutton(self, text="Year3", variable= self.varYear, value="Year3") 
    R3.grid(row=12, column= 1, sticky=W, padx=100)
    R4 = Radiobutton(self, text="Year4", variable= self.varYear, value="Year4") 
    R4.grid(row=13, column= 1, sticky=W, padx=100)

  def get_number(self):
    lblNumber = Label(self, text="Student Number:")
    lblNumber.grid(row=14, column=0)

    self.userNumber = IntVar()
    userNumber = Entry(self, textvariable=self.userNumber)
    userNumber.grid(row=14, column=1)


##### test code ######

def test_button(f):
    try:
      (a,b,c) = f.get_information()
      print(a,b,c)
    except TypeError:
      pass

def main():
  window = Tk()
  f1 = Home(window)
  f1.pack(side = TOP, padx =20, pady =20)
  btn = Button( window , text = 'Choose',
    command = lambda: test_button(f1))
  btn.pack(side = BOTTOM, padx =20, pady =20)
  window.mainloop()

if __name__ == '__main__':
  main()
