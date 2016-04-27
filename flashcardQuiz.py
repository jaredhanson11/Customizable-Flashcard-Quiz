
"""
	Runs the quiz, random or in order based on which is not function isn't commented out.
"""
def main():
	while True:
		try:
			textFileName = str(raw_input("Whats the path of to the text file containing your flashcards?\n"))
			flashcards = makeFlashCardDict(textFileName)
			inOrderGenerator(flashcards)
			#randomGenerator(flashcards)
		except OSError, e:
			continue





"""
	Returns dictionary with the terms as the keys and the definition as the
		values. The definition includes the topic, if available, and is formatted as
		'topic \n\n\n definition'. The dictionary only contains terms that are between 'start/n' 
		and 'end'n. Topics are non-empty lines thats don't contain a '-'. They are the topic
		for all of the following terms until a new topic overrides it.

	@input textFile has to be formatted for every term 'term - definition\n' where neither
		term nor defintion contain '-' or newline characters. Must contain "start\n" and "end\n"
		in that order.
	@throws TODO throws IOException
"""
def makeFlashCardDict(textFile):
	flashCards = {}
	start = False
	topic = "No Topic Provided\n"


	try:
		with open(textFile) as f:
			fileContent = f.readlines()
	except OSError, e:
		raise e
		

	for line in fileContent:
		if start != "start\n":
			start = line
			continue
		if line == "end\n":
			break
		if "-" in line:
			terms = line.split("-", 1)
			if terms[0][1]==" ":
				termList = terms[0].split(" ",1)
			else:
				termList = [None,terms[0]]
			definition = terms[1].lower()
			term = termList[len(termList)-1].lower()
			flashCards[term] = topic + definition
		else:
			if len(line.split()) >= 1:
				topic = line
	print "there are", len(flashCards.keys()), "terms"
	return flashCards


"""
	Takes a dictionary of flashCards and runs a program that quizes the
		user on their flashCards. Uses user input to see the definition and takes a random
		term from the dictionary everytime, but no term is ever given twice.
"""
def randomGenerator(flashCards):
	check = { i : 0 for i in flashCards}
	from random import sample
	origKeys = flashCards.keys()
	keys = flashCards.keys()
	x = ""
	# check = {}
	while x != "break":
		print "\n\n\n"
		term = sample(keys,1)[0]
		# if term not in check:
		# 	check[term] = 0
		# check[term] += 1

		#All this does is makes sure you don't get the same term twice in a row
		keys = flashCards.keys()
		keys.remove(term)
		print term
		# check[term] += 1
		x = raw_input("--------------------\n")
		print flashCards[term]
		x = raw_input("press enter for the next word or type 'break' to end")
	print check

"""
	Takes a dictionary of flashCards and runs a program that quizes the
		user on their flashCards. Uses user input to see the definition and goes in a random
		order all the way through the dictionary, then re-randomizes the terms and goes through 
		the terms again.
"""
def inOrderGenerator(flashCards):
	from random import shuffle
	keys = flashCards.keys()
	while True:
		shuffle(keys)
		count = 1
		for term in keys:
			print "\n\n\n term", count, "of", len(keys)
			print term
			x = raw_input("--------------------\n")
			print flashCards[term]
			x = raw_input("press enter for the next word")
			count+=1


main()


