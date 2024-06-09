
def f1(N, W, H, map_pieces):
    # Initialize a dictionary to store the map pieces
    map_pieces_dict = {}
    for i in range(N):
        map_pieces_dict[i+1] = map_pieces[i]
    
    # Initialize a list to store the reconstructed map
    reconstructed_map = []
    
    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        for j in range(H):
            for k in range(W):
                if map_pieces_dict[i][j][k] != " ":
                    reconstructed_map.append(map_pieces_dict[i][j][k])
    
    # Return the reconstructed map
    return "".join(reconstructed_map)

def f2(N, W, H, map_pieces):
    # Initialize a dictionary to store the map pieces
    map_pieces_dict = {}
    for i in range(N):
        map_pieces_dict[i+1] = map_pieces[i]
    
    # Initialize a list to store the reconstructed map
    reconstructed_map = []
    
    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        for j in range(H):
            for k in range(W):
                if map_pieces_dict[i][j][k] != " ":
                    reconstructed_map.append(map_pieces_dict[i][j][k])
    
    # Return the reconstructed map
    return "".join(reconstructed_map)

if __name__ == '__main__':
    N = int(input())
    W = int(input())
    H = int(input())
    map_pieces = []
    for i in range(N):
        map_pieces.append(input())
    reconstructed_map = f1(N, W, H, map_pieces)
    print(reconstructed_map)

