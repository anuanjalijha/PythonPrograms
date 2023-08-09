def isPermutation(string1, string2):
    # Remove spaces from both strings (if needed)
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    # Check if the lengths of the strings are equal
    if len(string1) != len(string2):
        return False

    # Convert strings to lists to allow character manipulation
    list1 = list(string1)
    list2 = list(string2)

    # Sort the lists using bubble sort (you can also use other sorting algorithms)
    for i in range(len(list1)):
        for j in range(len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]

    # Compare the sorted lists
    if list1 == list2:
        return True
    else:
        return False
