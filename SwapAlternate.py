def swapAlternate(arr, n):
        if len(arr)%2 !=0:
            for i in range(0, len(arr)-2, 2):


        # Swap elements at positions i and i+1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            for i in range(0, len(arr), 2):


        # Swap elements at positions i and i+1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


        return arr
