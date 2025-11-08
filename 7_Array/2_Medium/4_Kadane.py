arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def kadane(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    
    for x in arr[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

print(kadane(arr))