def twosum_exists(arr, target):
    arr.sort()  # sort array first, since two-pointer needs sorted input
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return "YES"
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return "NO"


# Example
arr = [2, 6, 5, 8, 11]
target = 14
print(twosum_exists(arr, target))  # Output: YES
