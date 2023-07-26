n = int(input())
i = 1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1

    spaces = 1
    while spaces<=(2*n)-(2*i):
        print(" ",end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print((i-j)+1,end='')
        j=j+1
    print()
    i=i+1
