def linearSearch(li,ele):
    for i in range(len(li)):
        if li[i]==ele:
            return i
    return -1
    
li = [1,2,3,6,5]
index = linearSearch(li,9)
print(index)