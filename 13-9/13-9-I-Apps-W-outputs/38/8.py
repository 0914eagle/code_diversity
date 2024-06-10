
def get_min_size(n):
    # Find the minimum size of the chessboard
    m = 1
    while m * m < n:
        m += 1
    return m

def place_pieces(n, m):
    # Place n pieces on a mxm chessboard
    pieces = [(i, i) for i in range(1, n+1)]
    for i in range(n):
        r1, c1 = pieces[i]
        for j in range(i+1, n):
            r2, c2 = pieces[j]
            if abs(r1 - r2) + abs(c1 - c2) < abs(i - j):
                pieces[j] = (r2, c2 - 1) if c2 > 1 else (r2 - 1, m)
    return pieces

def main():
    n = int(input())
    m = get_min_size(n)
    pieces = place_pieces(n, m)
    print(m)
    for piece in pieces:
        print(*piece)

if __name__ == '__main__':
    main()

