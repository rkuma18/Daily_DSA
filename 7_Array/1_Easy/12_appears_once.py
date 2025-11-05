def once(arr):
    result = 0
    for num in arr:
        result ^= num  # XOR cancels duplicates
    return result

arr = [4,1,2,1,2]
print(once(arr))
