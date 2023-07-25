n = int(input())
i = 1
while i<=n:
#     spaces
    spaces=1
    while spaces<=(n-i):
        print(" ",end='')
        spaces =spaces+1
#   increasing sequence      
    p=i    
    j=1    
    while j<=i:
        print(p,end='')
        j=j+1
        p=p+1
#    decreasing sequence 
    p = p-2
    while p>=i:
        print(p,end='')
        p=p-1
    
        
    print()
    i=i+1

