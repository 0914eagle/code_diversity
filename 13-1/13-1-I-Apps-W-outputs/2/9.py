
def max_beauty(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    # Split the matrix into 4 submatrices
    submatrices = []
    for i in range(0, n, n//2):
        for j in range(0, n, n//2):
            submatrices.append(matrix[i:i+n//2][j:j+n//2])

    # Find the maximum element in the matrix
    max_element = max(max(row) for row in matrix)

    # Calculate the beauty of each submatrix
    submatrix_beauties = []
    for submatrix in submatrices:
        submatrix_beauties.append(max_beauty(submatrix))

    # Return the maximum beauty of the matrix
    return max_element + sum(submatrix_beauties)

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

print(max_beauty(matrix))

