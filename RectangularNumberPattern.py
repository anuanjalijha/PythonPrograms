N = int(input())
 
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i<j:
            min=i
        else:
            min=j
        print(N - min + 1, end = " ")
 
    for j in range(N - 1, 0, -1):
        if i<j:
            min=i
        else:
            min=j
        print(N - min + 1, end = " ")
 
 
    print()
     
for i in range(N - 1, 0, -1):
    for j in range(1, N + 1):
        if i<j:
            min=i
        else:
            min=j
        print(N - min + 1, end = " ")
 
 
    for j in range(N - 1, 0, -1):
        if i<j:
            min=i
        else:
            min=j
        print(N - min + 1, end = " ")
 
 
    print()

