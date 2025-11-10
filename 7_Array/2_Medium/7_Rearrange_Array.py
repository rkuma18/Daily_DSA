'''
Problem Statement:

There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.
'''

def rearrange(arr):
    pos = []
    neg = []
    result = []

    # Separate positive and negative numbers
    for num in arr:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    
    print(f'Positive numbers: {pos}')
    print(f'Negative numbers: {neg}')

    # Merge alternately, starting with positive
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    
    return result

arr = [1, 2, -4, -5]
print(rearrange(arr))
