def largest(arr):
    result = sorted(arr)
    return result[-1]

def sortArr(arr):
    arr.sort()
    return arr[-1]
# O(Nlog(N))

def large_max(arr):
    result = max(arr)
    return result
# O(n)


arr= [8,10,5,7,9]
print('Largest element in a array:', largest(arr))



