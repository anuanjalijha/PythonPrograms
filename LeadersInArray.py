def find_leaders(arr, n):
    leaders = []
    max_right = arr[n - 1]  # The rightmost element is always a leader
    leaders.append(max_right)
    
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)
    
    leaders.reverse()  # Reverse the list to get the leaders in the original order
    return leaders

# Example usage
n = int(input())
arr = list(map(int, input().split()))

leader_elements = find_leaders(arr, n)
print( *leader_elements)
