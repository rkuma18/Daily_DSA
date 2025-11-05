def search(arr, nums):
    n = len(arr)
    for i in range(n):
        if arr[i] == nums:
            return i
    return -1  # Only reached if not found


arr = [1, 2, 3, 4, 5]
num = 3

print(search(arr, num))
