
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

        # Add the current map piece to the reconstructed map
        reconstructed_map.append(current_map)

    # Return the reconstructed map
    return reconstructed_map

def f2(reconstructed_map):
    # Initialize a dictionary to store the map pieces
    map_dict = {}

    # Loop through the reconstructed map and add the map pieces to the dictionary
    for i in range(len(reconstructed_map)):
        map_dict[i+1] = reconstructed_map[i]

    # Return the dictionary
    return map_dict

if __name__ == '__main__':
    # Test the functions
    N = 3
    W_list = [4, 2, 2]
    H_list = [1, 2, 2]
    map_list = ['2123', '21', '10', '23', '12']
    reconstructed_map = f1(N, W_list, H_list, map_list)
    map_dict = f2(reconstructed_map)
    print(map_dict)

