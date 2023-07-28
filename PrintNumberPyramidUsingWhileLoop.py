n = int(input())
n1 = n
n2 = n-1
i = 1 
while i<=n1:
    space = 1 
    while space<=i-1:
        print(" ",end='')
        space=space+1
    j=1
    while j<=(n1-i)+1:
        print((i+j)-1,end='')
        j=j+1 
    i=i+1 
    print()
i= n2
while i>=1:
    space=1
    while space<=i-1:
        print(" ",end='')
        space = space+1 
    j=1 
    while j<=(n2-i)+2:
        print((i+j)-1,end='')
        j=j+1
    i=i-1 
    print()
