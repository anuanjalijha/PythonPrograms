n = int(input())
i = 1
while i<=n:
    j=1
    start = chr(ord('A')+n-1)
    startChar = chr(ord(start)-i+1)
    while j<=i:
        charP=chr(ord(startChar)+j-1)
        print(charP,end='')
        j=j+1
         
    print()
    i=i+1
