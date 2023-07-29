def printTable(start,end,step):
    for i in range(start,end+1,step):
        c = int(5/9*(i-32))
        print(i,c)
	

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
