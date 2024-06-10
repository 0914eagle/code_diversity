
def get_min_board_size(n):
    # Find the smallest board size that can hold n pieces
    for m in range(1, n):
        if n % m == 0:
            return m
    return n

def place_pieces(n, m):
    # Place n pieces on an mxm board
    board = [[0] * m for _ in range(m)]
    pieces = [(i, i) for i in range(1, n+1)]
    for i in range(n):
        r, c = pieces[i]
        board[r-1][c-1] = i+1
    return board

def main():
    n = int(input())
    m = get_min_board_size(n)
    board = place_pieces(n, m)
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    main()

