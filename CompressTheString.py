
def getCompressedString(input) :
	
	
    compressed = ""
    count = 1
    
    for i in range(len(input)):
        if i == len(input) - 1 or input[i] != input[i + 1]:
            compressed += input[i] + (str(count) if count > 1 else "")
            count = 1
        else:
            count += 1
    
    return compressed
