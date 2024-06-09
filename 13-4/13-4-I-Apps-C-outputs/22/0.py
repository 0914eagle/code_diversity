
def f1(N, W_i, H_i, map_pieces):
    # Initialize a dictionary to store the map pieces
    map_pieces_dict = {}
    for i in range(N):
        map_pieces_dict[i+1] = map_pieces[i]
    
    # Initialize a list to store the reconstructed map
    reconstructed_map = []
    
    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        current_piece = map_pieces_dict[i+1]
        for j in range(len(current_piece)):
            reconstructed_map.append(current_piece[j])
    
    # Return the reconstructed map
    return reconstructed_map

def f2(reconstructed_map):
    # Initialize a dictionary to store the map pieces
    map_pieces_dict = {}
    
    # Loop through the reconstructed map and add the corresponding map pieces to the dictionary
    for i in range(len(reconstructed_map)):
        current_piece = reconstructed_map[i]
        map_pieces_dict[current_piece] = i+1
    
    # Return the dictionary
    return map_pieces_dict

if __name__ == '__main__':
    N = int(input())
    map_pieces = []
    for i in range(N):
        W_i, H_i = map(int, input().split())
        map_pieces.append(input())
    reconstructed_map = f1(N, W_i, H_i, map_pieces)
    map_pieces_dict = f2(reconstructed_map)
    print(str(len(reconstructed_map)) + " " + str(len(reconstructed_map[0])))
    for i in range(len(reconstructed_map)):
        print("".join(reconstructed_map[i]))
    print("-" * len(reconstructed_map[0]))
    for i in range(len(reconstructed_map)):
        print("".join(str(map_pieces_dict[reconstructed_map[i][j]]) for j in range(len(reconstructed_map[i]))))

