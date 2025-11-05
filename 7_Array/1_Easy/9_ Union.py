def union(arr1, arr2):
    seen = set()

    for i in arr1:
        seen.add(i)

    for j in arr2:
        seen.add(j)

    return list(seen)


arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]
print(union(arr1, arr2))