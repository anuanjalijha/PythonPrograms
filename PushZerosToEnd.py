
def pushZerosAtEnd(arr, n) :
    non_zero_count = 0

    # Move all non-zero elements to the left side
    for i in range(n):
        if arr[i] != 0:
            arr[non_zero_count] = arr[i]
            non_zero_count += 1

    # Fill the remaining elements with zeros
    while non_zero_count < n:
        arr[non_zero_count] = 0
        non_zero_count += 1


    return arr