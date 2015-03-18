from Choice import *
from Question import *

class Questionnaire:

	def __init__(self, inQuestionnaireID, inType):
		self.type = inType
		self.QuestionnaireID = inQuestionnaireID
		self.Questions = []

	def addQuestion(self, iQuestion):
		self.Questions.append(iQuestion)

	def printQuestionnaire(self):
		for question in self.Questions:
			print("")
			question.printQuestion()
			print("")


# Creating Questionnaire 1 ******************************************** Vark

Questionnaire1 = Questionnaire(1, "Vark")

newQuestion = Question(1, "How do you learn coding?")
newChoice = Choice("a", "Through visual examples on how to code.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Trial and error.", 4)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Having been taught through lectures and labs.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Reading back through a book to understand code.", 3)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(2, "When going through how a website works with a Web server do you prefer to:")
newChoice = Choice("a", "See a diagram.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Talk about it in a group.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Read through lecture notes.", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Build a website and host it on a web server.", 4)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(3, "When using a brand new IDE or any other software to allow coding, do you understand it by:")
newChoice = Choice("a", "Find an online or locally saved manual to learn the software.", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Play with the software and overtime learn how to use it.", 4)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Watching a video tutorial online to understand how it works.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Ask someone who has had experience with the software.", 2)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(4, "You are about to use a function from a new framework you found on the internet and you are not quite sure how it works. You will:")
newChoice = Choice("a", "Read the documentation given in the website of the framework.", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Check examples already done by somebody.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Call and ask a friend who has experience with this framework.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Try to figure out how it works by trial and error.", 4)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(5, "You are studying networking and wanted to revise, you see the different network topologies (e.g. Bus, Star and Ring) and decided to go over them, do you:")
newChoice = Choice("a", "Look at diagrams based on the topologies and learn from there.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Go to the nearest computer lab and try to analyse which topology the lab is using.", 4)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Go over your notes from the lecture (the notes consist of bullet points).", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "I understood the topologies after I attended the lecture.", 2)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)

newQuestion = Question(6, "If you are helping someone with a question where you need to solve a programming problem, you would:")
newChoice = Choice("a", "Go through the problem on the computers with the person.", 4)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Tell the person how to solve the problem.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Explain how to solve the problem with diagrams and arrows.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Write down pseudocode/code to help them solve the problem.", 3)
newQuestion.addChoice(newChoice)
Questionnaire1.addQuestion(newQuestion)




# Creating Questionnaire 2 ******************************************** H&M

Questionnaire2 = Questionnaire(2, "HM")

newQuestion = Question(1, "When learning what an Object is in object orientated programming do you prefer:")
newChoice = Choice("a", "To role-play a scenario.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Read a book about the subject.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Be given a relevant case study that applies in a working environment.", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Discuss in a group.", 4)
newQuestion.addChoice(newChoice)
Questionnaire2.addQuestion(newQuestion)

newQuestion = Question(2, "When given a task to develop a piece of software for an item of coursework, do you find it best to:")
newChoice = Choice("a", "Go straight into the problem with confidence of solving it.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Seek out some pre-existing software that is similar and use that as an example.", 4)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Get into a team / group and collectively solve the problem together.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Solving the problem over a period of time in small sections.", 3)
newQuestion.addChoice(newChoice)
Questionnaire2.addQuestion(newQuestion)

newQuestion = Question(3, "As a team you are about to start a software project for your new module and you need to come up with a proper computer language which you will use. In the team meeting you will:")
newChoice = Choice("a", "Start watching other teams solutions on the problem to help you with your decision.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Start a discussion about the language with your team members.", 4)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Think more about the algorithms which will be needed in the project to get the most efficient language.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Research what the last year students had used and pick the language with the most successful projects.", 3)
newQuestion.addChoice(newChoice)
Questionnaire2.addQuestion(newQuestion)

newQuestion = Question(4, "You have just received your first web applications coursework brief and you decide to start developing your website, you wanted to try positioning items in your website although you have not fully gone through it in class, you’re friends told you positioning items in the site is very hard, do you:")
newChoice = Choice("a", "Read about how you can position items online. ", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Keep on trying positioning items until you succeed.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Read how positioning items works before you try doing it.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Wait until you fully cover positioning in class and work on what you did in class later.", 4)
newQuestion.addChoice(newChoice)
Questionnaire2.addQuestion(newQuestion)

newQuestion = Question(5, "When learning new mathematical theory, do you prefer:")
newChoice = Choice("a", "Seeing the theory applied in the real world and seeing a purpose for it.", 3)
newQuestion.addChoice(newChoice)
newChoice = Choice("b", "Get stuck in and start doing lots of practice exercise.", 1)
newQuestion.addChoice(newChoice)
newChoice = Choice("c", "Learn the proof of the theory.", 2)
newQuestion.addChoice(newChoice)
newChoice = Choice("d", "Watch someone go through examples and work it out in your head.", 4)
newQuestion.addChoice(newChoice)
Questionnaire2.addQuestion(newQuestion)