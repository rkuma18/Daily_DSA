def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]          # the element to be inserted
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift elements to the right
            j -= 1
        arr[j + 1] = key        # place key at correct position
    return arr

arr = [13, 46, 24, 52, 20, 9]
print(insertion(arr))
