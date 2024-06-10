
def get_minimum_board_size(n):
    # Find the smallest value of m such that n chess pieces can be placed on a mxm chessboard
    m = 1
    while True:
        if m * m >= n:
            break
        m += 1
    return m

def place_pieces(n, m):
    # Place n chess pieces on a mxm chessboard with the given rule
    pieces = [(i, i) for i in range(1, n+1)]
    for i in range(n):
        for j in range(i+1, n):
            if abs(pieces[i][0] - pieces[j][0]) + abs(pieces[i][1] - pieces[j][1]) < abs(i - j):
                return None
    return pieces

def main():
    n = int(input())
    m = get_minimum_board_size(n)
    pieces = place_pieces(n, m)
    if pieces is None:
        print(-1)
    else:
        for piece in pieces:
            print(*piece)

if __name__ == '__main__':
    main()

