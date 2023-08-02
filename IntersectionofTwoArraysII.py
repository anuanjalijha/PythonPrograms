import sys
def find_intersection(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                print(arr1[i],end=" ")
                arr2[j]= sys.maxsize
                break
            


arr1 = [2,6,2,3,2]
arr2 = [3,2,2]
result = find_intersection(arr1, arr2)
print(result)  # Output: [3, 4, 5]
