def removeAllOccurrencesOfChar(string, ch) :
	li = []  # Split the sentence into word
	x = ""
    
	for char in string:
		if char!=ch:
			li.append(char)
    	
	for i in li:
		x+=i
	return x   
