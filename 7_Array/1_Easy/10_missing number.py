def missing(arr, N):

    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum


arr = [1, 2, 4, 5]
N = 5
print(missing(arr, N)) 