def highestOccuringChar(string) :
    max_count = 0
    max_char = None
    for char in string:
        count = string.count(char)
        if count>max_count:
            max_count=count
            max_char = char
    return max_char        
