def subarray(arr, total):
    current_sum = 0
    max_len = 0
    hashmap = {}  # prefix_sum → first index

    for i in range(len(arr)):
        current_sum += arr[i]

        # Case 1: entire subarray (0...i) sums to total
        if current_sum == total:
            max_len = i + 1

        # Case 2: subarray found between two prefix sums
        if (current_sum - total) in hashmap:
            prev_index = hashmap[current_sum - total]
            max_len = max(max_len, i - prev_index)

        # Store prefix sum if first time seen
        if current_sum not in hashmap:
            hashmap[current_sum] = i

    return max_len


arr = [10, 5, 2, 7, 1, 9]
k = 15
print(subarray(arr, k))
