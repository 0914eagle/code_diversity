
def get_map_pieces(N):
    map_pieces = []
    for i in range(N):
        W, H = map(int, input().split())
        map_pieces.append([input() for _ in range(H)])
    return map_pieces

def reconstruct_map(map_pieces):
    W, H = 0, 0
    for piece in map_pieces:
        W = max(W, len(piece[0]))
        H = max(H, len(piece))
    
    map_grid = [['0'] * W for _ in range(H)]
    for i, piece in enumerate(map_pieces):
        for y, row in enumerate(piece):
            for x, val in enumerate(row):
                map_grid[y + H - len(piece)][x + W - len(row)] = str(i + 1)
    
    return map_grid

def main():
    N = int(input())
    map_pieces = get_map_pieces(N)
    map_grid = reconstruct_map(map_pieces)
    print(W, H)
    for row in map_grid:
        print("".join(row))
    print("-" * W)
    for i in range(N):
        print("".join([str(i + 1) for _ in range(W)]))

if __name__ == '__main__':
    main()

