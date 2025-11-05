def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # slow pointer – tracks position of last unique element

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]  # move next unique element forward

    return i + 1  # number of unique elements
arr = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(arr)
print(k)         # 5
print(arr[:k])   # [0, 1, 2, 3, 4]
