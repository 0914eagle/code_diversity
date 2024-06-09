
def solve(s):
    # Initialize the matrix with -1
    matrix = [[-1] * 10 for _ in range(10)]

    # Fill in the matrix with the minimum number of digits to insert
    for i in range(10):
        for j in range(10):
            if i == 0 and j == 0:
                continue
            else:
                matrix[i][j] = min(len(s), len(str(i * j)) - len(str(i)) + len(s))

    return matrix

