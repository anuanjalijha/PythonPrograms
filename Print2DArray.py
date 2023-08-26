def print_arr(arr,n,m):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(n-i):
            for k in range(m):
                print(arr[i][k],end=" ")
            print() 
        print(end="")  

n, m = map(int, input().split())

# Taking input for the 2D array
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
print_arr(arr,n,m)    
