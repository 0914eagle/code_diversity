
def get_min_board_size(n):
    # Find the smallest board size that can hold n pieces
    for m in range(1, n):
        if m * m >= n:
            return m
    return n

def place_pieces(n, m):
    # Place n pieces on an mxm board
    pieces = [(i, i) for i in range(1, n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            if abs(pieces[i][0] - pieces[j][0]) + abs(pieces[i][1] - pieces[j][1]) < abs(i - j):
                return []
    return pieces

if __name__ == '__main__':
    n = int(input())
    m = get_min_board_size(n)
    pieces = place_pieces(n, m)
    if not pieces:
        print(-1)
    else:
        for piece in pieces:
            print(piece[0], piece[1])

