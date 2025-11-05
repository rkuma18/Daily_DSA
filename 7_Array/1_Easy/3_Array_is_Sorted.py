def SortedArray(arr):
    if arr == sorted(arr):
        return True
    else:
        return False
# O(n log n)

def SortedArrays(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
# O(n)

arr= [8,10,5,7,9]
print(SortedArrays(arr))