def majority(arr):
    # Phase 1: Find candidate
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Phase 2: Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


arr = [3, 2, 3]
print(majority(arr))