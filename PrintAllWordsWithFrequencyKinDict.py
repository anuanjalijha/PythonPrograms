def printKFreeqWords(s,k):
    words = s.split()
    d={}
    for w in words:
        if w in d:
            d[w]=d[w]+1 
        else:
            d[w]=1 
    for w in d:
        if d[w]==k:
            print(w)
s = "This is a word string having many many word" 
printKFreeqWords(s,2)