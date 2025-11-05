def moveZero(arr):
    n = len(arr)
    new = []
    rest = []
    for i in range(n):
        if arr[i] == 0:
            new.append(arr[i])
        else:
            rest.append(arr[i])
    
    rest.extend(new)   # modifies rest
    return rest



def moveZerot(arr):
    n = len(arr)
    left = 0  # Pointer to track where next non-zero should go

    # Step 1: Move all non-zero elements forward
    for i in range(n):
        if arr[i] != 0:
            arr[left] = arr[i]
            left += 1

    # Step 2: Fill the rest of the array with zeros
    for i in range(left, n):
        arr[i] = 0

    return arr


# Example
arr = [1, 0, 2, 3, 0, 4, 0, 1]
print(moveZerot(arr))
