def rotate(arr, k, right=True):
    n = len(arr)
    k = k % n 

    if right:  # Right rotation
        new = arr[-k:] + arr[:-k]
    else:      # Left rotation
        new = arr[k:] + arr[:k]
    return new


arr = [1, 2, 3, 4, 5]
n = 2

# Example 1: Left rotation
print(rotate(arr, n, right=False))  

# Example 2: Right rotation
print(rotate(arr, n, right=True))    
