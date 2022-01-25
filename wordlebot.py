# please dont read this code its so poorly optimised and commented lol

import enchant
d = enchant.Dict("en_UK")
availableLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]

dict2 = {"orange": {}, "green": {}}
wordsUsedCount = int(input("How many words used so far?:"))
wordsUsedArray = []
knownLettersArray = []
for i in range(wordsUsedCount):
	allDone = False
	wordUsed = input("Word used: ")
	wordsUsedArray.append(wordUsed)
	while allDone == False:
		result = input("Enter G/O (green/orange), letter used, and position in the word (1-5). Enter Q if complete:\n")
		if result == "Q" or result == "q":
			for i in list(wordUsed):
				
				if i not in dict2['orange'].keys() and i not in dict2['green'].keys():
					
					if i in availableLetters:
						availableLetters.remove(i)
			allDone = True
		else:
			result = result.split(" ")
			if result[0] == "G":
				dict2['green'][result[1]] = int(result[2])-1
				if result[1] not in dict2['orange'].keys():
					knownLettersArray.append(result[1])
				else:
					dict2['orange'].pop(result[1])
			elif result[0] == "O":
				if result[1] not in dict2['green'].keys():
					if result[1] in dict2['orange'].keys():
						dict2['orange'][result[1]].append(int(result[2])-1)
					else:
						dict2['orange'][result[1]] = []
						dict2['orange'][result[1]].append(int(result[2])-1)
						knownLettersArray.append(result[1])

knownLetters = len(knownLettersArray)

options = knownLetters

def findNextOptions(inputArray, letter):
	outputArray = []
	for i in inputArray:
		count = -1
		for char in i:
			count += 1
			if char == "-":
				if letter not in dict2['green'].keys():
					if letter not in dict2['orange'].keys():
						i[count] = str(letter)
						outputArray.append(list(i))
						i[count] = "-"
					elif int(count) not in dict2['orange'][letter]:
						i[count] = str(letter)
						outputArray.append(list(i))
						i[count] = "-"
				elif int(dict2['green'][letter]) == int(count):
					i[count] = str(letter)
					outputArray.append(list(i))
					i[count] = "-"

	return outputArray

def findInitialOptions():
	startArray = ["-", "-", "-", "-", "-"]
	outputArray = []
	for i in range(5):
		if startArray[i] == "-":
			
			if knownLettersArray[options-1] not in dict2['green'].keys():
				if knownLettersArray[options-1] not in dict2['orange'].keys():
					startArray[i] = knownLettersArray[options-1]
					outputArray.append(list(startArray))
					startArray[i] = "-"
				elif int(i) not in dict2['orange'][knownLettersArray[options-1]]:
					startArray[i] = knownLettersArray[options-1]
					outputArray.append(list(startArray))
					startArray[i] = "-"
			elif int(dict2['green'][knownLettersArray[options-1]]) == int(i):
				startArray[i] = knownLettersArray[options-1]
				outputArray.append(list(startArray))
				startArray[i] = "-"

	return outputArray
	
firstArray = findInitialOptions()
currentArray = []
options -= 1
while options > 0:
	firstArray = findNextOptions(firstArray, knownLettersArray[options-1])
	
	options -= 1

inputLetters = availableLetters
options = firstArray
secondOptions = []
thirdOptions = []
fourthOptions = []
finalResults = []

optionCount = 0

def findOutputs(initialOptions):
	optionsOutput = []
	for option in initialOptions:
	# For each of the possible remaining letters
		for letter in inputLetters:
			# Set index to -1
			charCount = -1
			# For each of the letters in the combination possibility
			for char in option:
				# Increase letter index
				charCount += 1
				# If the letter is blank (i.e. == "-")
				if char == "-":
					if letter not in dict2['orange'].keys():
						if letter not in dict2['green'].keys():
							testArr = option
							testArr[charCount] = letter
							optionsOutput.append(list(testArr))
							testArr[charCount] = "-"
							testArr = []
						elif charCount == dict2['green'][letter]:
							testArr = option
							testArr[charCount] = letter
							optionsOutput.append(list(testArr))
							testArr[charCount] = "-"
							testArr = []
					elif charCount not in dict2['orange'][letter]:
						testArr = option
						testArr[charCount] = letter
						optionsOutput.append(list(testArr))
						testArr[charCount] = "-"
						testArr = []
	return optionsOutput
finalResultsArray = {}
optionsOutput = findOutputs(firstArray)
write = False
if (5-knownLetters-1) > 0:
	for i in range(5-knownLetters-1):
		optionsOutput = findOutputs(optionsOutput)
		if "-" not in list(optionsOutput[0]):
			write = True
		finalResultsCount = 0
		if write == True:
			for fourthOption in optionsOutput:
				testStr = ""
				for i in fourthOption:
					testStr += i
				if d.check(testStr) == True:
					if testStr not in finalResults:
						finalResultsCount += 1
						finalResults.append(testStr)
						print(str(finalResultsCount) + ": " + testStr)
						finalResultsArray[finalResultsCount] = testStr
else:
	finalResultsCount = 0
	for fourthOption in optionsOutput:
		testStr = ""
		for i in fourthOption:
			testStr += i
		if d.check(testStr) == True:
			if testStr not in finalResults:
				finalResultsCount += 1
				finalResults.append(testStr)
				print(str(finalResultsCount) + ": " + testStr)
				finalResultsArray[finalResultsCount] = testStr
print("\n")
chosenResults = input("Enter spaced digits of words to take through: ")
wordsInput = []
print("\n")
for i in chosenResults.split(" "):
	print("CHOSEN: " + finalResultsArray[int(i)])
	wordsInput.append(finalResultsArray[int(i)])
print("\n")
wordsInputDictionary = {}
inverseDictionary = {}

for word in wordsInput:
	wordsInputDictionary[word] = {}
	inverseDictionary[word] = {}

	for otherWord in wordsInput:
		if otherWord != word:
			inverseDictionary[word][otherWord] = {}
			count = -1
			for letter in list(word):
				count += 1
				if list(otherWord)[count] == letter:
					inverseDictionary[word][otherWord][letter] = "Green"
				else:
					if letter in list(otherWord):
						inverseDictionary[word][otherWord][letter] = "Amber"

finalDictionary = {}

for word in inverseDictionary.keys():
	finalDictionary[word] = {}
	for otherWord in inverseDictionary[word].keys():
		finalDictionary[word][otherWord] = ""
		tempStr = ""
		for character in inverseDictionary[word][otherWord].keys():
			tempStr += character + inverseDictionary[word][otherWord][character]
		finalDictionary[word][otherWord] = tempStr	

mostUniqueCount = 0
mostUnique = []
wordCount = 0
for word in finalDictionary.keys():
	wordCount += 1
	uniqueArray = []
	uniqueCount = 0
	for otherWord in finalDictionary[word]:
		if finalDictionary[word][otherWord] not in uniqueArray:
			uniqueArray.append(finalDictionary[word][otherWord])
			uniqueCount += 1
	if uniqueCount > mostUniqueCount:
		mostUniqueCount = uniqueCount
		mostUnique = []
		mostUnique.append(word)
	elif uniqueCount == mostUniqueCount:
		mostUnique.append(word)
print("\nBest words to use next:")
print(mostUnique)
if (wordCount - 1) == mostUniqueCount:
	print("Guaranteed to confirm correct word in the next go.")
else:
	print("Not guaranteed to confirm correct word in the next go.")

# START WITH: NOTES, ACRID
