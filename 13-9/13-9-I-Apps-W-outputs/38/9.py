
def get_smallest_chessboard(n):
    for m in range(1, n+1):
        if m * m >= n:
            return m
    return -1

def place_pieces(n, m):
    pieces = [(i, i) for i in range(1, n+1)]
    return pieces

if __name__ == '__main__':
    n = int(input())
    m = get_smallest_chessboard(n)
    if m != -1:
        pieces = place_pieces(n, m)
        for piece in pieces:
            print(piece[0], piece[1])
    else:
        print(-1)

