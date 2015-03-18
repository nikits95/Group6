import displayStyle

class CalResults:
	def __init__(self, data, learningType):
		self.data = data
		self.type = learningType
		if learningType == "Honey & Mumford":
			results = self.calculateOccurance(data)
			self.learningType = self.selectTypeHoneyStlye(results)
		else:
			results = self.calculateOccurance(data)
			self.learningType = self.selectTypeVARKStlye(results)	

	def getType(self):	
		return self.learningType

	def calculateOccurance(self, data):
		occurance = []
		for i in [1,2,3,4]:
			results = self.numberCounter(data,i)
			occurance.append(results)
		numMax = 1
		compare = 0
		for i in range(0,3):
			if(occurance[i] > compare):
				compare = occurance[i]
				numMax = i

		typeOfLearningStyle = numMax+1
		return typeOfLearningStyle
	
	def selectTypeHoneyStlye(self, number):
		if number == 1:
			return "Reflector"
		elif number == 2:
			return "Pragmatist"
		elif number == 3:
			return "Theorist"
		else:
			return "Activist"

	def selectTypeVARKStlye(self, number):
		if number == 1:
			return "Visual" #will change them to return after testing
		elif number == 2:
			return "Kinesthetic"
		elif number == 3:
			return "Aural"
		else:
			return "Reading"

	def numberCounter(self,data,number):
		numTimes = 0
		for i in data:
			if i == number:
				numTimes+= 1
		return numTimes


##### test code ######

def main():
	test1 = CalResults([2,1,1,3,3,3,3,4], "H&M")
	print(test1.getType())
	test2 = CalResults([2,4,4,2,1,2,2,1], "VARK")
	print(test2.getType())

if __name__ == "__main__":
	main()
