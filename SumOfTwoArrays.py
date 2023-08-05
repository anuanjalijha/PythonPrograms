def sumOfTwoArrays(arr1, n, arr2, m, output):
    carry = 0
    i = n - 1
    j = m - 1
    k = max(n, m)

    while k >= 0:
        sum_ = carry

        if i >= 0:
            sum_ += arr1[i]
        if j >= 0:
            sum_ += arr2[j]

        output[k] = sum_ % 10
        carry = sum_ // 10

        i -= 1
        j -= 1
        k -= 1

    # If there's still a carry after the loop, add it to the output
    if carry > 0:
        output[0] = carry

# Input and Output handling
if __name__ == "__main__":
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        try:
            n = int(input().strip())
            arr1 = list(map(int, input().strip().split()))
            m = int(input().strip())
            arr2 = list(map(int, input().strip().split()))
        except ValueError:
            print(0)  # Handle the case when both arrays are empty
            continue

        output_size = max(n, m) + 1
        output = [0] * output_size

        sumOfTwoArrays(arr1, n, arr2, m, output)

        # If the result is [0, 0, 0, ...], print just one 0.
        if all(digit == 0 for digit in output):
            print(0)
        else:
            for digit in output:
                print(digit, end=" ")
            print()
