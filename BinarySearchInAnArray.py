li = [1,2,3,4,5,6,7]
target = 9
l = 0
u = len(li)-1
position = -1
while l<=u:
    mid = (l+u)//2
    if(li[mid]==target):
        position = mid
        break
    if target>li[mid]:
        l = mid+1
    else:
        u = mid-1
if(position!=-1):
    print(position)
else:
    print("key is not found")
       
