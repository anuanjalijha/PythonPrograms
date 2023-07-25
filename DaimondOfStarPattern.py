n = int(input())
n1 = (n+1)//2
n2 = n//2
i=1
# first half
while i<=n1:
    space =1
    while space<=n1-i:
        print(" ",end='')
        space=space+1
    j=1
    while j<=(2*i)-1:
        print("*",end='')
        j=j+1    
    print()
    i=i+1
    #  second half
i = n2
while i>=1:
    space = 1
    while space<=(n2-i)+1:
        print(" ",end='')
        space=space+1
    j=1
    while j<=(2*i)-1:
        print("*",end='')
        j=j+1    
    print()
    i=i-1    