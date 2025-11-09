def max_subarray_with_sum(arr):
    current_sum = max_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        # If starting fresh gives better sum, reset current_sum and s
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        # Update max_sum and indices if we found a new maximum
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    print(f"Maximum Subarray Sum: {max_sum}")
    print(f"Subarray: {arr[start:end+1]}")
    return max_sum, arr[start:end+1]


# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_with_sum(arr)
