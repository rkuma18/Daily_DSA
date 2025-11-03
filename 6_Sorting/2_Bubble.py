def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # use a flag to track swapping
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # mark that a swap happened
        if not swapped:  # no swaps → array already sorted
            break
    return arr

arr = [13, 46, 24, 52, 20, 9]
print(bubble(arr))
