n = int(input())
n1 = n
n2 = n-1
 
for i in range(1,n1+1):
    for s in range(1,i):
        print(" ",end='')
        
    for j in range(1,(n1-i)+2):
        print((i+j)-1,end='')
         
    print()

for i in range(n2,0,-1):
    
    for s in range(1,i):
        print(" ",end='')
         
     
    for j in range(1,(n2-i)+3):
        print((i+j)-1,end='')
        
    print()
