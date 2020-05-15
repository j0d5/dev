from numpy import random

baseArray = list(range(0, 100))
randomArray = []

while len(randomArray) < len(baseArray):
	randomValue = baseArray[random.randint(100)]
	if randomValue in randomArray:
		continue
	else:
		randomArray.append(randomValue)
	
print(randomArray)
