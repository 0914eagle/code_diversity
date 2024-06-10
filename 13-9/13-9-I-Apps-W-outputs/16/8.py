
def check_winning_move(n, m, moves):
    # Initialize a 2D array to store the color of each pixel
    field = [[0] * m for _ in range(n)]

    # Loop through each move and color the corresponding pixel
    for i, j in moves:
        field[i - 1][j - 1] = 1

    # Check if a 2x2 square of black pixels is formed
    for i in range(n - 1):
        for j in range(m - 1):
            if field[i][j] == 1 and field[i][j + 1] == 1 and field[i + 1][j] == 1 and field[i + 1][j + 1] == 1:
                return True
    return False

def find_losing_move(n, m, moves):
    # Loop through each move and check if it results in a losing state
    for i in range(len(moves)):
        if check_winning_move(n, m, moves[:i + 1]):
            return i + 1
    return 0

def main():
    n, m, k = map(int, input().split())
    moves = []
    for _ in range(k):
        moves.append(list(map(int, input().split())))
    print(find_losing_move(n, m, moves))

if __name__ == '__main__':
    main()

