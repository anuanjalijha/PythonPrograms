def sumUnique(l):
    s=set()
    for i in l:
        s.add(i)
    sum=0
    for i in s:
        sum+=i 
    return sum    
print(sumUnique([1,2,3,4,4,3,4,2,1,5,5]))    