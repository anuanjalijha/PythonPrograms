def findTriplet(arr,m):
    count=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                
                if arr[i]+arr[j]+arr[k]==m:
                    count= count+1 
    return count 
arr = [2,-5,8,-6,0,5,10,11,-3]
m = 10
x = findTriplet(li,m)
print(x)
