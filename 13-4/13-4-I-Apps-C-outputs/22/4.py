
def get_map_pieces(N):
    map_pieces = []
    for i in range(N):
        W, H = map(int, input().split())
        map_pieces.append([input() for _ in range(H)])
    return map_pieces

def reconstruct_map(map_pieces):
    W, H = get_map_pieces_dimensions(map_pieces)
    map_grid = [[0 for _ in range(W)] for _ in range(H)]
    for i, piece in enumerate(map_pieces):
        for j, row in enumerate(piece):
            for k, value in enumerate(row):
                map_grid[j][k] = (i+1) % 10
    return map_grid

def get_map_pieces_dimensions(map_pieces):
    W = max(len(piece[0]) for piece in map_pieces)
    H = max(len(piece) for piece in map_pieces)
    return W, H

def print_map(map_grid):
    print(f"{len(map_grid[0])} {len(map_grid)}")
    for row in map_grid:
        print("".join(str(value) for value in row))
    print("-" * len(map_grid[0]))
    for i, piece in enumerate(map_pieces):
        print("".join(str(i+1) for row in piece for _ in row))

if __name__ == '__main__':
    N = int(input())
    map_pieces = get_map_pieces(N)
    map_grid = reconstruct_map(map_pieces)
    print_map(map_grid)

