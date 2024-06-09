
def f1(N, W_list, H_list, map_list):
    # Initialize a dictionary to store the map pieces
    map_dict = {}
    for i in range(N):
        map_dict[i+1] = map_list[i]
    
    # Initialize a list to store the reconstructed map
    reconstructed_map = []
    
    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        # Get the current map piece
        current_map = map_dict[i+1]
        
        # Get the width and height of the current map piece
        current_width = W_list[i]
        current_height = H_list[i]
        
        # Add the current map piece to the reconstructed map
        for j in range(current_height):
            reconstructed_map.append(current_map[j])
    
    # Return the reconstructed map
    return reconstructed_map

def f2(reconstructed_map):
    # Initialize a dictionary to store the map pieces
    map_dict = {}
    
    # Loop through the reconstructed map and add the map pieces to the dictionary
    for i in range(len(reconstructed_map)):
        # Get the current square
        current_square = reconstructed_map[i]
        
        # Get the map piece index for the current square
        map_piece_index = current_square % 10
        
        # Add the map piece index to the dictionary
        map_dict[map_piece_index] = map_dict.get(map_piece_index, 0) + 1
    
    # Return the dictionary
    return map_dict

if __name__ == '__main__':
    # Read the input
    N = int(input())
    W_list = []
    H_list = []
    map_list = []
    for i in range(N):
        W, H = map(int, input().split())
        W_list.append(W)
        H_list.append(H)
        map_list.append(input())
    
    # Call f1 to reconstruct the map
    reconstructed_map = f1(N, W_list, H_list, map_list)
    
    # Call f2 to get the map pieces
    map_dict = f2(reconstructed_map)
    
    # Print the width and height of the reconstructed map
    print(max(W_list), max(H_list))
    
    # Print the reconstructed map
    for i in range(max(H_list)):
        print("".join(reconstructed_map[i*max(W_list):(i+1)*max(W_list)]))
    
    # Print the map pieces
    for i in range(1, N+1):
        print("-"*max(W_list))
        for j in range(map_dict[i]):
            print("".join([str(i)]*max(W_list)))

