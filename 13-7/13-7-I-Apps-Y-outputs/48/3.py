
def is_symmetric(matrix):
    return matrix == matrix.T

def can_construct_square(n, m, tiles):
    # Initialize a matrix to store the tiles
    matrix = [[0] * m for _ in range(m)]

    # Loop through each tile type
    for tile in tiles:
        # Check if the tile can be placed in the matrix
        for i in range(m - 1):
            for j in range(m - 1):
                if matrix[i][j] == 0 and matrix[i + 1][j] == 0 and matrix[i][j + 1] == 0 and matrix[i + 1][j + 1] == 0:
                    matrix[i][j] = tile[0]
                    matrix[i + 1][j] = tile[1]
                    matrix[i][j + 1] = tile[2]
                    matrix[i + 1][j + 1] = tile[3]
                    break
            else:
                continue
        else:
            return False

    # Check if the matrix is symmetric
    return is_symmetric(matrix)

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        tiles = []
        for _ in range(n):
            tile = list(map(int, input().split()))
            tiles.append(tile)
        if can_construct_square(n, m, tiles):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

