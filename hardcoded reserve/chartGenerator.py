from tkinter import *
import numpy as np
import pickle
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def myplotcode(data):
    f = Figure(figsize=(5,4), dpi=100)
    ax = f.add_subplot(111)

    ## the data
    N = 8
    results = []
    V, A, R, K, Ref, Pra, The, Act = 0, 0, 0, 0, 0, 0, 0, 0

    for r in data:
        if r[4] == "Visual":
            V = V + 1
        elif r[4] == "Aural":
            A = A + 1
        elif r[4] == "Kinesthetic":
            K = K + 1
        else:
            R = R + 1
        if r[3] == "Reflector":
            Ref = Ref + 1
        elif r[3] == "Pragmatist":
            Pra = Pra + 1
        elif r[3] == "Theorist":
            The = The + 1
        else:
            Act = Act + 1

    results.append(V)
    results.append(A)
    results.append(R)
    results.append(K)
    results.append(Ref)
    results.append(Pra)
    results.append(The)
    results.append(Act)

    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.35                      # the width of the bars

    ## the bars
    rects1 = ax.bar(ind, results, width,
                color='black',
                error_kw=dict(elinewidth=2,ecolor='red'))

    # axes and labels
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0, max(results) + 5)
    ax.set_ylabel('Students')
    ax.set_title('Overall results')
    xTickMarks = ["V", "A", "R", "K", "Ref", "Pra", "The", "Act"]
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)

    return f

class mygui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.data_table=[]
        file = open( "pickle.dat", "rb" )
        self.data_table = pickle.load(file)
        file.close()


        self.fig = myplotcode(self.data_table)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.show()

        self.canvas.get_tk_widget().pack()
        self.pack(fill=BOTH, expand=1)

    def stopGraph(self):
        self.canvas.get_tk_widget().destroy()

def main():
    root = Tk()
    app = mygui(root)
    root.mainloop()

if __name__ == "__main__":
    main()