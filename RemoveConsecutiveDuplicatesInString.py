def removeConsecutiveDuplicates(string) :
	x = ""
	result = []
	previous = None
	for char in string:
	    if char!=previous:
	        result.append(char)
	        previous = char
	
	for i in result:
	    x+=i
	return x
