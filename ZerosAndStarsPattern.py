n = int(input())
i=1
while i<=n:
    j = 1
    while j<=(2*n)+1:
        if i==j or j==(2*n+2)//2 or i+j==2*n+2:
            print("*",end='')
        else:
            print(0,end='')
        j=j+1    
    print()
    i=i+1