'''
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
'''



def rotate_in_place(matrix):
    n = len(matrix)

    # Step 1: Transpose in place
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rotate_in_place(matrix)
print(matrix)


