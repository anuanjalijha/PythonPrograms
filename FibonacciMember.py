def checkMember(n):
    a, b = 0, 1
    while a<n:
        a, b = b, a + b
    return a==n




n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")