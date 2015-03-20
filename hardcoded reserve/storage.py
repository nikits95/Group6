import pickle
import os

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
    #data.add_data(1998999, "CS", "Year 1", "Pragmatic", "Visual") 
    data.print_out_data()

if __name__ == '__main__':
    main()
