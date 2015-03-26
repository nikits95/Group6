import displayStyle

class CalResults:
	def __init__(self, data, learningType):
		self.data = data
		self.type = learningType
		#calls relevent methods for calculating results
		if learningType == "Honey & Mumford":
			results = self.calculateOccurance(data)
			self.learningType = self.selectTypeHoneyStlye(results)
		else:
			#VARK part
			results = self.calculateOccurance(data)
			self.learningType = self.selectTypeVARKStlye(results)	

	def getType(self):	
		return self.learningType

	def calculateOccurance(self, data):
		#this function calculates the results by counting 
		#the number of times it occurs
		occurance = []
		for i in [1,2,3,4]:
			results = self.numberCounter(data,i)
			occurance.append(results)
		numMax = 1
		compare = 0
		for i in range(0,3):
			if occurance[i] > compare:
				compare = occurance[i]
				numMax = i

		typeOfLearningStyle = numMax+1 # 1 is added as list starts at 0 where the results start at 1 
		return typeOfLearningStyle
	
	def selectTypeHoneyStlye(self, number):
		#converts to the learning style
		if number == 1:
			return "Theorist"
		elif number == 2:
			return "Reflector" 
		elif number == 3:
			return "Pragmatist" 
		else:
			return "Activist"

	def selectTypeVARKStlye(self, number):
		#converts to the learning style
		if number == 1:
			return "Visual" 
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
	test1 = CalResults([1,1,2,2,3], "Honey & Mumford")
	print(test1.getType())
	test2 = CalResults([2,4,4,2,1,2,2,1], "VARK")
	print(test2.getType())

if __name__ == "__main__":
	main()
