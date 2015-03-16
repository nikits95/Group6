class CalResults:
	def __init__(self, data,typeQ):
		self.data = data
		self.typeQ = typeQ
		print("The inforamton is : " + str(self.data))
		if self.typeQ == "H&M":
			self.honeyMumford(self.data)
		else:
			print("-----")

	def honeyMumford(self, data):
		#print("HoneyMumford")
		occurance = {}
		for i in [1,2,3,4]:
			#print("Number : "+ str(i))
			results = self.numberCounter(data,i)
			
			occurance.update({i:results})
		print(occurance)

		#for key, item in occurance.items():
			#print(key, item)

	def numberCounter(self,data,number):
		numTimes = 0
		for i in data:
			#print("Compareing :"+str(i))
			if i == number:
				numTimes+= 1
		return numTimes

#CalResults([2,4,2,1], "H&M") - For testing purposes