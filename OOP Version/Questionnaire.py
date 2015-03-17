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
