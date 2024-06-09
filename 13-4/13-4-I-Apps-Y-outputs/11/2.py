
def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def can_construct_square(n, m, tiles):
    # Initialize a matrix of size m x m
    matrix = [[0 for _ in range(m)] for _ in range(m)]

    # Fill the matrix with the tiles
    for i in range(n):
        for j in range(n):
            matrix[i][j] = tiles[i][0]
            matrix[i][m-j-1] = tiles[i][1]
            matrix[m-i-1][j] = tiles[i][2]
            matrix[m-i-1][m-j-1] = tiles[i][3]

    # Check if the matrix is symmetric
    return is_symmetric(matrix)

tiles = []
n, m = map(int, input().split())
for i in range(n):
    tiles.append(list(map(int, input().split())))

print("YES") if can_construct_square(n, m, tiles) else print("NO")

