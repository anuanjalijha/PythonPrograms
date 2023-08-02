def pairSum(arr,x) :
    count=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==x:
                count= count+1 
    return count 
