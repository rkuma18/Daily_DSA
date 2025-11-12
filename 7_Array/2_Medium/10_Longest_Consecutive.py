'''
Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.
'''

def longest_consecutive(arr):
    num_set = set(arr)
    longest = 0

    for num in num_set:
        # Check if num is the start of a sequence
        if num - 1 not in num_set:
            length = 1
            current = num
            # Count consecutive numbers
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

    return longest

arr = [100, 200, 1, 3, 2, 4]
print(longest_consecutive(arr))
