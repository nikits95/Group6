import pickle
import os
import tkinter.messagebox

class storage:
    def __init__(self):
        if not os.path.isfile('pickle.dat'):
            self.data_table=[]
        else:
            self.retrive()

    def add_data(self, number, degreeType, year, HMType, VARKType):
        row=[number, year, degreeType, HMType, VARKType]
        self.data_table.append(row)
        self.store()

    def print_out_data(self):
        for r in self.data_table:
            print(r[0], r[1], r[2], r[3], r[4])

    def print_out_vark(self, year, degreeType):
        V = 0
        A = 0
        R = 0
        K = 0
        
        for r in self.data_table:
            if r[2] == degreeType and r[1] == year :  
                if r[4] == "Visual":
                    V = V + 1
                elif r[4] == "Aural":
                    A = A + 1
                elif r[4] == "Reading":
                    R = R + 1
                elif r[4] == "Kinesthetic":
                    K = K + 1
        if V == 1:
            s = "Student"
        else:
            s = "Students"  

        if A == 1:
            st = "Student"
        else:
            st = "Students"

        if R == 1:
            stu = "Student"
        else:
            stu = "Students"
            
        if K == 1:
            stud = "Student"
        else:
            stud = "Students"                       
                        
        v = "Visual: " +  str(V) + " " + s
        a = "Aural: " + str(A) + " " + st
        r = "Reading: " + str(R) + " " + stu 
        k = "Kinesthetic: " + str(K) + " " + stud

        n = V + A + R + K

        c = "There were " + str(n) + " Students who took the questionnaire where:"
        tkinter.messagebox.showinfo("Analysis", c + "\n" + "\n" +  v + "\n" + a + "\n" + r + "\n" + k )

    def print_out_ALL(self, year, degreeType):
        R = 0
        P = 0
        T = 0
        A = 0

        V = 0
        A = 0
        R = 0
        K = 0

        for r in self.data_table: 
            if r[3] == "Reflector":
                R = R + 1
            elif r[3] == "Pragmatist":
                P = P + 1
            elif r[3] == "Theorist":
                T = T + 1
            elif r[3] == "Activist":
                A = A + 1
                        
        r= "Reflector: " + str(R) + " " + "student"
        p = "Pragmatist: " +  str(P) + " " + "student"
        t = "Theorist: " + str(T) + " " + "student"
        a = "Activist " + str(A) + " " + "student"

        
        for r in self.data_table:  
            if r[4] == "Visual":
                V = V + 1
            elif r[4] == "Aural":
                A = A + 1
            elif r[4] == "Reading":
                R = R + 1
            elif r[4] == "Kinesthetic":
                K = K + 1
                        
        v = "Visual: " +  str(V) + " " + "student"
        a = "Aural: " + str(A) + " " + "student" 
        r = "Reading: " + str(R) + " " + "student" 
        k = "Kinesthetic: " + str(K) + " " + "student"

        n = V + A + R + K + R + P + T + A

        c = "There were " + str(n) + " Students who took the questionnaire where:"

        tkinter.messagebox.showinfo("Analysis",  c + "\n" + "\n" +v + "\n" + a + "\n" + r + "\n" + k +"\n" + "\n" + r + "\n" + p + "\n" + t + "\n" + a)

    def print_out_HM(self, year, degreeType):
        R = 0
        P = 0
        T = 0
        A = 0

        for r in self.data_table:
            if r[2] == degreeType and r[1] == year :  
                if r[3] == "Reflector":
                    R = R + 1
                elif r[3] == "Pragmatist":
                    P = P + 1
                elif r[3] == "Theorist":
                    T = T + 1
                elif r[3] == "Activist":
                    A = A + 1

        n = R + P + T + A

        c = "There were " + str(n) + " Students who took the questionnaire where:"
        
        if R == 1:
            s = "Student"
        else:
            s = "Students"  

        if P == 1:
            st = "Student"
        else:
            st = "Students"

        if T == 1:
            stu = "Student"
        else:
            stu = "Students"
            
        if A == 1:
            stud = "Student"
        else:
            stud = "Students"            
                        
        r= "Reflector: " + str(R) + " " + s
        p = "Pragmatist: " +  str(P) + " " + st
        t = "Theorist: " + str(T) + " " + stu
        a = "Activist " + str(A) + " " + stud

        tkinter.messagebox.showinfo("Analysis", c + "\n" + "\n" +  r + "\n" + p + "\n" + t + "\n" + a)


    def store(self):
        file = open( "pickle.dat", "wb" )
        pickle.dump(self.data_table,file )
        file.close()

    def retrive(self):
        file = open( "pickle.dat", "rb" )
        self.data_table = pickle.load(file)
        file.close()
        



def main():
    data = storage()
    #data.add_data(1998999, "BIS", "Year1", "Pragmatic", "Visual")
    #data.add_data(1998999, "Joints", "Year1", "Activist", "Kinetic") 
    #data.add_data(1998999, "CS", "Year2", "Pragmatic", "Aural")
    #data.add_data(1998999, "CS", "Year2", "Pragmatic", "Visual")  
    #data.add_data(1998999, "CS", "Year3", "Pragmatic", "Visual")  
    #data.add_data(1998999, "Joints", "Year1", "Pragmatic", "Visual") 
    data.print_out_data()

if __name__ == '__main__':
    main()
