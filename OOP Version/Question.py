class Question:

	def __init__(self, inQuestionId, inQuestionContent):
		self.QuestionId = inQuestionId
		self.QuestionContent = inQuestionContent
		self.Choices = []

	def addChoice(self, inChoice):
		self.Choices.append(inChoice)

	def printQuestion(self):
		print(str(self.QuestionId) + ". " + str(self.QuestionContent))
		for choice in self.Choices:
			choice.printChoice()

