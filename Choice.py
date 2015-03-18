class Choice:

	def __init__(self, inChoiceId, inChoiceContent, inIsTrue):
		self.ChoiceId = inChoiceId
		self.ChoiceContent = inChoiceContent
		self.IsTrue = inIsTrue

	def printChoice(self):
		print(str(self.ChoiceId) + ") " + str(self.ChoiceContent))

	def checkChoice(self):
		print(self.IsTrue)