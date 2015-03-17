from Choice import *
from Question import *
from Questionnaire import * 
from tkinter import *

Questionnaire1 = Questionnaire(1, "Vark")

newQuestion = Question(1, "How do you learn coding?")
newChoice = Choice("a", "Through visual examples on how to code.", True)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Trial and error.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Having been taught through lectures and labs.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Reading back through a book to understand code.", False)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(2, "When going through how a website works with a Web server do you prefer to:")
newChoice = Choice("a", "See a diagram.", True)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Talk about it in a group.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Read through lecture notes.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Build a website and host it on a web server.", False)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(3, "When using a brand new IDE or any other software to allow coding, do you understand it by:")
newChoice = Choice("a", "Find an online or locally saved manual to learn the software.", True)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Play with the software and overtime learn how to use it.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Watching a video tutorial online to understand how it works.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Ask someone who has had experience with the software.", False)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(4, "You are about to use a function from a new framework you found on the internet and you are not quite sure how it works. You will:")
newChoice = Choice("a", "Read the documentation given in the website of the framework.", True)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Check examples already done by somebody.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Call and ask a friend who has experience with this framework.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Try to figure out how it works by trial and error.", False)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(5, "You are studying networking and wanted to revise, you see the different network topologies (e.g. Bus, Star and Ring) and decided to go over them, do you:")
newChoice = Choice("a", "Look at diagrams based on the topologies and learn from there.", True)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Go to the nearest computer lab and try to analyse which topology the lab is using.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Go over your notes from the lecture (the notes consist of bullet points).", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "I understood the topologies after I attended the lecture.", False)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(6, "If you are helping someone with a question where you need to solve a programming problem, you would:")
newChoice = Choice("a", "Go through the problem on the computers with the person.", True)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Tell the person how to solve the problem.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Explain how to solve the problem with diagrams and arrows.", False)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Write down pseudocode/code to help them solve the problem.", False)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)


print("")
print("")
Questionnaire1.printQuestionnaire()
print("")

class Application(Frame):

    def nextQ(self, root, frame, i):
        frame.destroy()
        self.createWidgets(root, i)

    def createWidgets(self, root, i):
        self.frame = Frame(root)
        self.frame.pack()
        self.question = Questionnaire1.Questions[i]
        self.label = Label(self.frame, justify="left", text=(str(self.question.QuestionId) + ". " + self.question.QuestionContent + "\n"))
        self.label.pack(side="top", anchor="w")
        for choice in self.question.Choices:
            self.r = Radiobutton(self.frame, text=(str(choice.ChoiceId) + ". " + choice.ChoiceContent + "\n"), variable=self.question.QuestionId, value=choice.ChoiceId)
            self.r.select()
            self.r.pack(side="top", anchor="w", padx=100)
        print("a")
        self.b = Button(self.frame, text="Next", command=lambda: self.nextQ(root, self.frame, i+1))
        self.b.pack()
        self.label.pack()
        self.label.bind("<1>", quit)

    def __init__(self, master):
        self.root = master # root is a passed Tk object
        self.createWidgets(self.root, 0)

root = Tk()
root.geometry("1000x300")
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
app = Application(master=root)
root.mainloop()
root.destroy()
