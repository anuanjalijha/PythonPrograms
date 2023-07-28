n = int(input())
n1 = (n+1)//2
n2 = n//2

# first half
for i in range(1,n1+1):
    for s in range(1,(n1-i)+1):
        print(" ",end='')
        
    for j in range(1,2*i):
        print("*",end='')
            
    print()
    
    #  second half

for i in range(n2,0,-1):
    
    for s in range(1,(n2-i)+2):
        print(" ",end='')
        
    for j in range(1,2*i):
        print("*",end='')
            
    print()
       