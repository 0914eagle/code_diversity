
def get_min_size(n):
    # Find the minimum size of the chessboard
    for m in range(1, n):
        if n % m == 0:
            return m
    return n

def place_pieces(n, m):
    # Place the pieces on the chessboard
    pieces = [(i, j) for i in range(1, m+1) for j in range(1, m+1)]
    return pieces[:n]

def main():
    n = int(input())
    m = get_min_size(n)
    pieces = place_pieces(n, m)
    print(m)
    for piece in pieces:
        print(*piece)

if __name__ == '__main__':
    main()

