'''
Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.
'''
def leader(arr):
    result = []
    n = len(arr)
    max_from_right = arr[-1]   # last element is always a leader
    result.append(max_from_right)

    # Move from right to left
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            result.append(arr[i])
            max_from_right = arr[i]

    # reverse to get leaders in left-to-right order
    result.reverse()
    return result

arr = [16, 17, 4, 3, 5, 2]
print(leader(arr))  # Output: [17, 5, 2]

