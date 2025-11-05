def rotate(arr):
    n = len(arr)
    temp = arr[0]

    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[n-1] = temp

    return arr

arr = [1, 2, 3, 4, 5]
print(rotate(arr))