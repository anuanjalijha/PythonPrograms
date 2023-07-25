n = int(input())
i = 1
while i<=n:
#     spaces
    spaces=1
    while spaces<=(n-i):
        print(" ",end='')
        spaces =spaces+1
#   increasing sequence          
    j=1    
    while j<=i:
        print("*",end='')
        j=j+1
        
#    decreasing sequence 
    p = i-1
    while p>=1:
        print("*",end='')
        p=p-1
    
        
    print()
    i=i+1

        
        


