n = int(input())
i = 1
while i<=n:
#     spaces
    spaces=1
    while spaces<=(n-i):
        print(" ",end='')
        spaces =spaces+1
#   first sequence      
    
    j=1    
    while j<=i:
        print((i-j)+1,end='')
        j=j+1
        
        
#    second sequence 

    p = 2
    while p<=i:
        print(p,end='')
        p=p+1
    
        
    print()
    i=i+1