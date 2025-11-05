def longest_subarray_sum_k(arr, k):
    current_sum = 0
    max_len = 0
    prefix_map = {}  # prefix_sum → first index

    for i in range(len(arr)):
        current_sum += arr[i]

        # Case 1: If entire array (till i) sums to k
        if current_sum == k:
            max_len = i + 1

        # Case 2: If there's a previous prefix sum giving sum k
        if (current_sum - k) in prefix_map:
            length = i - prefix_map[current_sum - k]
            max_len = max(max_len, length)

        # Case 3: Store first occurrence of prefix_sum
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_len


# Example
arr = [-1, 1, 1]
k = 1
print(longest_subarray_sum_k(arr, k))  