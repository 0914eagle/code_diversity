
def get_map_pieces(N):
    pieces = []
    for i in range(N):
        W, H = map(int, input().split())
        piece = []
        for j in range(H):
            piece.append(list(input()))
        pieces.append(piece)
    return pieces

def assemble_map(pieces):
    W = len(pieces[0][0])
    H = len(pieces[0])
    map = [[0] * W for _ in range(H)]
    for i in range(N):
        piece = pieces[i]
        for j in range(H):
            for k in range(W):
                map[j][k] += piece[j][k] % 10
    return map

def get_map_piece_indices(map):
    indices = []
    for i in range(N):
        piece = pieces[i]
        for j in range(H):
            for k in range(W):
                if map[j][k] % 10 == piece[j][k]:
                    indices.append(i + 1)
    return indices

def main():
    N = int(input())
    pieces = get_map_pieces(N)
    map = assemble_map(pieces)
    indices = get_map_piece_indices(map)
    print(W, H)
    for i in range(H):
        print("".join(map[i]))
    print("-" * W)
    for i in range(H):
        print("".join(str(indices[i * W + j]) for j in range(W)))

if __name__ == '__main__':
    main()

