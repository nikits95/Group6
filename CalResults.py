import displayStyle

class CalResults:
	def __init__(self, data,typeQ):
		self.data = data
		self.typeQ = typeQ
		if self.typeQ == "H&M":
			self.honeyMumford(self.data)
		else:
			self.VARK(self.data)

	def honeyMumford(self, data):
		results = self.calculateOccurance(data)
		learningType = self.selectTypeHoneyStlye(results)
		displayStyle.main(learningType, "Honey & Mumford")

	def VARK(self,data):
		results = self.calculateOccurance(data)
		learningType = self.selectTypeVARKStlye(results)
		displayStyle.main(learningType, "VARK")

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

#CalResults([2,4,4,2,1,2,2,1], "H&M") #for testing, comment out if in use
#CalResults([2,4,4,2,1,2,2,1], "VARK")