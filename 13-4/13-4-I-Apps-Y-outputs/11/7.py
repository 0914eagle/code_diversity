
def is_symmetric(square):
    for i in range(len(square)):
        for j in range(i+1, len(square[0])):
            if square[i][j] != square[j][i]:
                return False
    return True

def can_construct_square(n, m, tiles):
    # Initialize a square of size m x m with all elements set to 0
    square = [[0] * m for _ in range(m)]

    # Iterate through each tile type and place it in the square
    for tile in tiles:
        # Check if the tile can be placed in the square
        for i in range(m - 1):
            for j in range(m - 1):
                if square[i][j] == 0 and square[i + 1][j] == 0 and square[i][j + 1] == 0 and square[i + 1][j + 1] == 0:
                    # Place the tile in the square
                    square[i][j] = tile[0]
                    square[i + 1][j] = tile[1]
                    square[i][j + 1] = tile[2]
                    square[i + 1][j + 1] = tile[3]
                    break
            else:
                continue
        else:
            return False

    # Check if the square is symmetric
    return is_symmetric(square)

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

