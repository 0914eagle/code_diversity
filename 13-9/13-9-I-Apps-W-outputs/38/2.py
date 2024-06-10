
def get_min_chessboard_size(n):
    # Find the minimum value of m such that m^2 >= n
    m = int(n**0.5) + 1
    return m

def place_pieces(n, m):
    # Initialize the chessboard
    chessboard = [[0 for _ in range(m)] for _ in range(m)]
    
    # Place the pieces on the chessboard
    for i in range(1, n+1):
        r = i
        c = i
        while chessboard[r-1][c-1] != 0:
            r += 1
            c += 1
        chessboard[r-1][c-1] = i
    
    # Return the coordinates of the pieces
    return [(r, c) for r in range(1, m+1) for c in range(1, m+1) if chessboard[r-1][c-1] != 0]

if __name__ == '__main__':
    n = int(input())
    m = get_min_chessboard_size(n)
    pieces = place_pieces(n, m)
    print(m)
    for piece in pieces:
        print(piece[0], piece[1])

