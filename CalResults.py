class CalResults:
	def __init__(self, data,typeQ):
		self.data = data
		self.typeQ = typeQ
		#print("The inforamton is : " + str(self.data))
		if self.typeQ == "H&M":
			self.honeyMumford(self.data)
		else:
			self.VARK(self.data)

	def VARK(self,data):
		print("")

	def honeyMumford(self, data):
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
		self.selectTypeHoneyStlye(typeOfLearningStyle)
	
	def selectTypeHoneyStlye(self, number):
		if number == 1:
			print("Reflector")
		elif number == 2:
			print("Pragmatist")
		elif number == 3:
			print("Theorist")
		else:
			print("Activist")

	def numberCounter(self,data,number):
		numTimes = 0
		for i in data:
			if i == number:
				numTimes+= 1
		return numTimes

#CalResults([2,4,4,2,1,2,2,1], "H&M")