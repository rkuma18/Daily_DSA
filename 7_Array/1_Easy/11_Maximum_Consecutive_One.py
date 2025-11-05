def maxOne(arr):
    n = len(arr)
    count = 0
    max_count = 0

    for i in range(n):
        if arr[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


arr = [1, 0, 1, 1, 0, 1]
print(maxOne(arr))
