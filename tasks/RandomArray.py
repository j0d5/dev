from numpy import random
import time

sizeOfArray = 100

def simpleUniqueRandomArray(size):
	randomArray = []
	while len(randomArray) < size:
		randomValue = random.randint(size)
		if randomValue in randomArray:
			continue
		else:
			randomArray.append(randomValue)
	return randomArray

start = time.clock()
print ("\nsimpleUniqueRandomArray:\n", simpleUniqueRandomArray(sizeOfArray))
print ("\nExecution time:" , time.clock() - start)

def setUniqueRandomArray(size):
	randomArray = []
	uniqueSet = set()
	
	while len(randomArray) < size:
		randomValue = random.randint(size)
		if randomValue in uniqueSet:
			continue
		else:
			uniqueSet.add(randomValue)
			randomArray.append(randomValue)
	return randomArray

start = time.clock()
print ("\nsetUniqueRandomArray:\n", setUniqueRandomArray(sizeOfArray))
print ("\nExecution time:" , time.clock() - start)

def shuffleUniqueRandomArray(size):
	randomArray = list(range(0, size))

	return random.randint(size, size=(size))

start = time.clock()
print ("\nshuffleUniqueRandomArray:\n", shuffleUniqueRandomArray(sizeOfArray))
print ("\nExecution time:" , time.clock() - start)
