from Choice import *
from tkinter import *
from Question import *
from Questionnaire import * 

class Application:

    def nextQ(self, root, quest, frame, i, v):
        frame.destroy()
        self.results.append(v)
        self.loadNextQuestion(root, quest, i)

    def loadNextQuestion(self, root, quest, i):
        if i >= len(quest.Questions):
            self.generateResult(root)
            return
        self.frame = Frame(root)
        self.frame.pack()
        self.question = quest.Questions[i]
        self.label = Label(self.frame, justify="left", text=(str(self.question.QuestionId) + ". " + self.question.QuestionContent + "\n"))
        self.label.pack(side="top", anchor="w")
        self.v = IntVar()
        for choice in self.question.Choices:
            self.r = Radiobutton(self.frame, text=(str(choice.ChoiceId) + ". " + choice.ChoiceContent + "\n"), variable=self.v, value=choice.IsTrue)
            self.r.select()
            self.r.pack(side="top", anchor="w", padx=100)
        self.b = Button(self.frame, text="Next", command=lambda: self.nextQ(root, quest, self.frame, i+1, self.v.get()))
        self.b.pack()
        self.label.pack()
        self.label.bind("<1>", quit)

    def loadMenu(self, root, frame):
        frame.destroy()
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, justify="left", text=("Click to start Questionnaire" + "\n"))
        self.label.pack(side="top", anchor="w")
        self.b = Button(self.frame, text="Vark", command=lambda: self.startQuestionnaire(root, self.frame, self.VQuestionnaire))
        self.b.pack()
        self.b = Button(self.frame, text="HM", command=lambda: self.startQuestionnaire(root, self.frame, self.HMQuestionnaire))
        self.b.pack()
        self.label.pack()
        self.label.bind("<1>", quit)


    def generateResult(self, root):
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, justify="left", text=("Your result is:" + "\n\n"))
        self.label.pack(side="top", anchor="w")
        self.label = Label(self.frame, justify="left", text=(self.results))
        self.label.pack(side="top", anchor="w")
        self.label.pack()
        self.label.bind("<1>", quit)

    def startQuestionnaire(self, root, frame, Questionnaire):
        frame.destroy()
        self.loadNextQuestion(root, Questionnaire, 0)

    def login(self, root):
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, justify="left", text=("Login as:" + "\n"))
        self.label.pack(side="top", anchor="w")
        self.b = Button(self.frame, text="Student", command=lambda: self.studentLogin(root, self.frame))
        self.b.pack()
        self.b = Button(self.frame, text="Staff", command=lambda: self.staffLogin(root, self.frame))
        self.b.pack()
        self.label.pack()
        self.label.bind("<1>", quit)

    def studentLogin(self, root, frame):
        frame.destroy()
        self.results = []
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, justify="left", text=("Student number:"))
        self.label.pack(side="top", anchor="w")
        self.e = Entry(self.frame)
        self.e.pack()
        self.label = Label(self.frame, justify="left", text=("Course of study:"))
        self.label.pack(side="top", anchor="w")
        self.variable = StringVar(self.frame)
        self.variable.set("Computer Science") # default value
        self.w = OptionMenu(self.frame, self.variable, "Computer Science", "Software Engineering", "Business information systems")
        self.w.pack()
        self.label = Label(self.frame, justify="left", text=("Year of study:"))
        self.label.pack(side="top", anchor="w")
        self.variable = StringVar(self.frame)
        self.variable.set("first") # default value
        self.w = OptionMenu(self.frame, self.variable, "first", "second", "thirt")
        self.w.pack()
        self.label = Label(self.frame, justify="left", text=("\n"))
        self.label.pack(side="top", anchor="w")
        self.b = Button(self.frame, text="Login", command=lambda: self.loadMenu(root, self.frame))
        self.b.pack()
        self.label.pack()
        self.label.bind("<1>", quit)

    def staffLogin(self, root, frame):
        frame.destroy()
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, justify="left", text=("Lecturer name:"))
        self.label.pack(side="top", anchor="w")
        self.e = Entry(self.frame)
        self.e.pack()
        self.label = Label(self.frame, justify="left", text=("Password:"))
        self.label.pack(side="top", anchor="w")
        self.e = Entry(self.frame)
        self.e.pack()
        self.label = Label(self.frame, justify="left", text=("\n"))
        self.label.pack(side="top", anchor="w")
        self.b = Button(self.frame, text="Login", command=lambda: self.loadStaffResults(root, self.frame))
        self.b.pack()
        self.label.pack()
        self.label.bind("<1>", quit)

    def loadStaffResults(self, root, frame):
        frame.destroy()
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, justify="left", text=("The overall results are:" + "\n"))
        self.label.pack(side="top", anchor="w")
        self.label.pack()
        self.label.bind("<1>", quit)


    def __init__(self, master, VQuest, HMQuest):
        self.root = master # root is a passed Tk object
        self.VQuestionnaire = VQuest
        self.HMQuestionnaire = HMQuest
        self.login(self.root)
