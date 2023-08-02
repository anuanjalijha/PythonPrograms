def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1

        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# Test the function
arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
sorted_arr = sort_binary_array(arr)
print(sorted_arr)  # Output: [0, 0, 0, 0, 0, 1
