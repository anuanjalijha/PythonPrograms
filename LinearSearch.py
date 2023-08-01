n = int(input())
flag = False 
li = [int(x) for x in input().split()]
ele = int(input())
for i in range(len(li)):
    if li[i]==ele:
        print(i)
        flag = True
        break
if flag is False:
    print(-1)
        