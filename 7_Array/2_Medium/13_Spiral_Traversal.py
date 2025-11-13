'''
Problem Statement: Given a Matrix, print the given matrix in spiral order.
'''

def spiral_order(matrix):
    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # 1. Traverse from Left → Right (top row)
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 2. Traverse from Top → Bottom (right column)
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Check again to avoid duplicates
        if top <= bottom:
            # 3. Traverse from Right → Left (bottom row)
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # 4. Traverse from Bottom → Top (left column)
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(spiral_order(matrix))
