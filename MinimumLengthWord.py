def minimum_length(str):
    words = str.split()
    shortest_word = words[0]
    for word in words:
        if(len(word))<len(shortest_word):
            shortest_word = word 
    return shortest_word
str = input() 
print(minimum_length(str))           

