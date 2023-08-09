
def reverseEachWord(string) :
	li = string.split()  # Split the sentence into words
	reversed_words = []
	x = ""
	for char in li:
		reversed_word = char[::-1]
		reversed_words.append(reversed_word)
    
	for i in reversed_words:
		x = x+i+" "
	return x   
